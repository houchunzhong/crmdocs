"""RAG knowledge base — Query the search index (hybrid retrieval + rerank)."""

import sys
import json

import numpy as np

from rag.config import BM25_INDEX_FILE, VECTOR_INDEX_FILE, RERANK_CANDIDATES
from rag.retriever import BM25Retriever, HybridRetriever
from rag.embeddings import rerank

# Force UTF-8 on Windows consoles
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def retrieve(query: str, top_n: int = RERANK_CANDIDATES) -> list[dict]:
    """Hybrid-retrieve top_n candidates, rerank them, return top-5 chunks."""
    if not BM25_INDEX_FILE.exists() or not VECTOR_INDEX_FILE.exists():
        raise FileNotFoundError(
            "Index files missing. Run 'python -m rag.ingest' first."
        )

    bm25 = BM25Retriever.load(str(BM25_INDEX_FILE))
    vectors = np.load(VECTOR_INDEX_FILE)

    hybrid = HybridRetriever(bm25, vectors)
    candidates = hybrid.search(query, top_n=top_n)  # [(idx, rrf_score)]

    if not candidates:
        return []

    # Rerank candidates with the cross-encoder for final precision.
    texts = [bm25.chunks[idx]["content"] for idx, _ in candidates]
    scores = rerank(query, texts)

    ranked = sorted(zip(candidates, scores), key=lambda x: x[1], reverse=True)[:5]

    results = []
    for (idx, _rrf_score), rerank_score in ranked:
        chunk = dict(bm25.chunks[idx])
        chunk["score"] = rerank_score
        results.append(chunk)
    return results


def format_result(r: dict, i: int) -> str:
    lines = [
        f"{'='*60}",
        f"[{i}] {r['title']}  |  §{r['section_number']} {r['section_title']}",
        f"    File: {r['file']}  |  Score: {r['score']:.4f}",
        f"{'─'*60}",
        r['content'][:800],
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m rag.query \"your question here\"", file=sys.stderr)
        sys.exit(1)

    query = sys.argv[1]

    try:
        results = retrieve(query)
    except FileNotFoundError as e:
        print(str(e), file=sys.stderr)
        sys.exit(1)

    if not results:
        print("No results found.")
        return

    # Output JSON for machine consumption (stdout must be pure JSON)
    if "--json" in sys.argv:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return

    print(f"\nTop {len(results)} results for: \"{query}\"\n")
    for i, r in enumerate(results, 1):
        print(format_result(r, i))
        print()


if __name__ == "__main__":
    main()
