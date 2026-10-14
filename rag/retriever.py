"""RAG knowledge base — BM25 retriever + hybrid (dense + sparse) retrieval."""

import re
import math
import pickle
from collections import Counter

import numpy as np

from rag.embeddings import embed


class BM25Retriever:
    """Pure-Python BM25 retriever with Chinese bigram support."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.chunks: list[dict] = []
        self.doc_terms: list[Counter] = []
        self.doc_len: list[int] = []
        self.avgdl: float = 0
        self.idf: dict[str, float] = {}
        self._built = False

    def _tokenize(self, text: str) -> list[str]:
        """Tokenize text. Uses bigrams for CJK, whitespace-split for ASCII."""
        tokens = []
        for part in re.split(r"([一-鿿]+)", text.lower()):
            if not part:
                continue
            if re.match(r"[一-鿿]", part[0]):
                # Chinese: character bigrams
                tokens.extend(part[i:i+2] for i in range(len(part)-1))
                tokens.append(part[-1])
            else:
                # English: split on non-alphanumeric
                tokens.extend(t for t in re.findall(r"[a-z0-9]+", part) if len(t) > 1)
        return tokens

    def build(self, chunks: list[dict]):
        self.chunks = chunks
        self.doc_terms = []
        self.doc_len = []
        N = len(chunks)

        for chunk in chunks:
            tokens = self._tokenize(chunk["content"])
            self.doc_terms.append(Counter(tokens))
            self.doc_len.append(len(tokens))

        self.avgdl = sum(self.doc_len) / N if N else 0

        # Compute IDF
        df = Counter()
        for dt in self.doc_terms:
            df.update(dt.keys())

        self.idf = {
            term: math.log((N - freq + 0.5) / (freq + 0.5) + 1.0)
            for term, freq in df.items()
        }
        self._built = True

    def rank(self, query: str, k: int | None = None) -> list[tuple[int, float]]:
        """Return (chunk_index, score) pairs sorted by score desc, optionally top-k."""
        if not self._built:
            return []

        query_tokens = self._tokenize(query)
        if not query_tokens:
            return []

        scores = []
        for i, dt in enumerate(self.doc_terms):
            score = 0.0
            for token in query_tokens:
                if token not in self.idf:
                    continue
                tf = dt.get(token, 0)
                score += (
                    self.idf[token]
                    * (tf * (self.k1 + 1))
                    / (tf + self.k1 * (1 - self.b + self.b * self.doc_len[i] / self.avgdl))
                )
            if score > 0:
                scores.append((i, score))

        scores.sort(key=lambda x: x[1], reverse=True)
        if k is not None:
            scores = scores[:k]
        return scores

    def search(self, query: str, k: int = 5) -> list[dict]:
        """Return top-k chunks with scores."""
        results = []
        for idx, score in self.rank(query, k=k):
            chunk = dict(self.chunks[idx])
            chunk["score"] = score
            results.append(chunk)
        return results

    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump({
                "chunks": self.chunks,
                "doc_terms": self.doc_terms,
                "doc_len": self.doc_len,
                "avgdl": self.avgdl,
                "idf": self.idf,
                "k1": self.k1,
                "b": self.b,
            }, f)

    @classmethod
    def load(cls, path: str) -> "BM25Retriever":
        with open(path, "rb") as f:
            data = pickle.load(f)
        retriever = cls(k1=data["k1"], b=data["b"])
        retriever.chunks = data["chunks"]
        retriever.doc_terms = data["doc_terms"]
        retriever.doc_len = data["doc_len"]
        retriever.avgdl = data["avgdl"]
        retriever.idf = data["idf"]
        retriever._built = True
        return retriever


class HybridRetriever:
    """BM25 (sparse) + dense vector retrieval, fused with Reciprocal Rank Fusion."""

    def __init__(self, bm25: BM25Retriever, vectors: np.ndarray):
        self.bm25 = bm25
        self.vectors = vectors  # (N, D), L2-normalized

    def search(self, query: str, top_n: int = 20) -> list[tuple[int, float]]:
        """Return (chunk_index, fused_rrf_score) pairs sorted desc, length <= top_n."""
        if len(self.vectors) != len(self.bm25.chunks):
            # Dense index missing/stale — fall back to sparse-only ranking.
            return self.bm25.rank(query, k=top_n)

        # 1. Sparse (BM25) ranking
        bm25_ranked = self.bm25.rank(query, k=top_n)

        # 2. Dense (vector) ranking
        qv = embed([query])[0]
        dense_scores = self.vectors @ qv  # dot product == cosine (normalized)
        dense_order = np.argsort(-dense_scores)[:top_n]

        # 3. RRF fusion
        rrf: dict[int, float] = {}
        for rank, (idx, _score) in enumerate(bm25_ranked):
            rrf[idx] = rrf.get(idx, 0.0) + 1.0 / (60 + rank + 1)
        for rank, idx in enumerate(dense_order):
            idx = int(idx)
            rrf[idx] = rrf.get(idx, 0.0) + 1.0 / (60 + rank + 1)

        return sorted(rrf.items(), key=lambda x: x[1], reverse=True)[:top_n]
