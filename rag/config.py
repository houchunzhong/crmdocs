"""RAG knowledge base configuration."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MD_DIR = BASE_DIR / "md"
ZH_CN_DIR = BASE_DIR / "zh-cn"
RAG_DATA_DIR = BASE_DIR / "rag_data"
CHUNKS_FILE = RAG_DATA_DIR / "chunks.json"
BM25_INDEX_FILE = RAG_DATA_DIR / "bm25_index.pkl"
VECTOR_INDEX_FILE = RAG_DATA_DIR / "vectors.npy"

# Semantic retrieval models (sentence-transformers)
# Downloaded from ModelScope (for networks where HuggingFace is blocked) via:
#   python -m rag.download_models
MODELS_DIR = RAG_DATA_DIR / "models"
EMBED_MODEL_PATH = MODELS_DIR / "bge-m3"
RERANK_MODEL_PATH = MODELS_DIR / "bge-reranker-v2-m3"
# Number of candidates recalled by the hybrid retriever before reranking
RERANK_CANDIDATES = 20

# Section header patterns: EN uses "## **N. Title**", CN uses "## **N、Title**"
SECTION_PATTERNS = [
    r"^##\s+\*\*(\d+)\.\s+(.+?)\*\*",    # EN: "## **1. Overview**"
    r"^##\s+\*\*([一二三四五六七八九十]+)、(.+?)\*\*",  # CN: "## **一、概述**"
]
