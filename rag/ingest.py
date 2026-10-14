"""RAG knowledge base — Ingest markdown files and build search index."""

import json
import sys

import numpy as np

from rag.config import (
    MD_DIR,
    ZH_CN_DIR,
    RAG_DATA_DIR,
    CHUNKS_FILE,
    BM25_INDEX_FILE,
    VECTOR_INDEX_FILE,
    EMBED_MODEL_PATH,
)
from rag.chunker import chunk_all
from rag.retriever import BM25Retriever
from rag.embeddings import embed

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    print("Ingesting CRM documentation...")

    RAG_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Step 1: Chunk all markdown files
    print(f"  Scanning {MD_DIR} and {ZH_CN_DIR}...")
    chunks = chunk_all(MD_DIR, ZH_CN_DIR)
    print(f"  Found {len(chunks)} sections across documents.")

    if not chunks:
        print("ERROR: No chunks found. Check your md/ and zh-cn/ directories.", file=sys.stderr)
        sys.exit(1)

    # Step 2: Save chunks as JSON
    with open(CHUNKS_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"  Saved chunks to {CHUNKS_FILE}")

    # Step 3: Build BM25 index
    print("  Building BM25 index...")
    retriever = BM25Retriever()
    retriever.build(chunks)
    retriever.save(str(BM25_INDEX_FILE))
    print(f"  Saved BM25 index to {BM25_INDEX_FILE}")

    # Step 4: Build dense vector index
    print(f"  Embedding {len(chunks)} chunks with {EMBED_MODEL_PATH.name}...")
    vectors = embed([c["content"] for c in chunks])
    np.save(VECTOR_INDEX_FILE, vectors)
    print(f"  Saved vector index {vectors.shape} to {VECTOR_INDEX_FILE}")

    en = sum(1 for c in chunks if c["language"] == "en")
    zh = sum(1 for c in chunks if c["language"] == "zh")
    print(f"Done. {en} English + {zh} Chinese chunks indexed.")


if __name__ == "__main__":
    main()
