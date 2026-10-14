"""Download bge models from ModelScope (for networks where HuggingFace is blocked).

Usage:
    python -m rag.download_models
"""

import sys

from rag.config import MODELS_DIR, EMBED_MODEL_PATH, RERANK_MODEL_PATH

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MODELS = {
    "BAAI/bge-m3": EMBED_MODEL_PATH,
    "BAAI/bge-reranker-v2-m3": RERANK_MODEL_PATH,
}


def _is_ready(path) -> bool:
    return path.exists() and any(path.iterdir())


def main():
    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    from modelscope import snapshot_download

    for model_id, dest in MODELS.items():
        if _is_ready(dest):
            print(f"  [skip] {model_id} already at {dest}")
            continue
        print(f"  Downloading {model_id} -> {dest} ...")
        snapshot_download(model_id, local_dir=str(dest))
        print(f"  Done: {dest}")

    print("All models ready.")


if __name__ == "__main__":
    main()
