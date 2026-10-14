"""RAG knowledge base — embedding & rerank models.

Lazy-loads sentence-transformers models as process-wide singletons so the
(first, slow) load cost is paid only once per process. Models are expected to
live in rag_data/models/ (see rag/download_models.py).
"""

import numpy as np

_embed_model = None
_rerank_model = None


def _missing(model_path) -> bool:
    return not model_path.exists() or not any(model_path.iterdir())


def get_embed_model():
    global _embed_model
    if _embed_model is None:
        from sentence_transformers import SentenceTransformer
        from rag.config import EMBED_MODEL_PATH
        if _missing(EMBED_MODEL_PATH):
            raise FileNotFoundError(
                f"Embedding model not found at {EMBED_MODEL_PATH}. "
                "Run 'python -m rag.download_models' first."
            )
        _embed_model = SentenceTransformer(str(EMBED_MODEL_PATH))
    return _embed_model


def get_rerank_model():
    global _rerank_model
    if _rerank_model is None:
        from sentence_transformers import CrossEncoder
        from rag.config import RERANK_MODEL_PATH
        if _missing(RERANK_MODEL_PATH):
            raise FileNotFoundError(
                f"Rerank model not found at {RERANK_MODEL_PATH}. "
                "Run 'python -m rag.download_models' first."
            )
        _rerank_model = CrossEncoder(str(RERANK_MODEL_PATH))
    return _rerank_model


def embed(texts, batch_size=32, normalize=True) -> np.ndarray:
    """Encode texts to L2-normalized vectors (dot product == cosine)."""
    model = get_embed_model()
    vectors = model.encode(
        texts,
        batch_size=batch_size,
        normalize_embeddings=normalize,
        show_progress_bar=False,
    )
    return np.asarray(vectors, dtype="float32")


def rerank(query: str, texts: list[str]) -> list[float]:
    """Score each text's relevance to the query (higher == more relevant)."""
    model = get_rerank_model()
    pairs = [[query, t] for t in texts]
    return [float(s) for s in model.predict(pairs)]
