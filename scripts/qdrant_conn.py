"""Qdrant Cloud connection for every rag-bench script.

Credentials come only from QDRANT_URL and QDRANT_API_KEY in the environment, or from a
KEY=VALUE file named by RAG_BENCH_ENV_FILE (kept outside the repo). Nothing is printed.
"""
import os

from qdrant_client import QdrantClient

MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DIM = 384
COLLECTION = "rag_bench_se_1m"


def _load():
    path = os.environ.get("RAG_BENCH_ENV_FILE")
    if path and os.path.exists(path):
        for line in open(path, encoding="utf-8"):
            if "=" in line:
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v)
    return os.environ["QDRANT_URL"], os.environ["QDRANT_API_KEY"]


def client(timeout=120):
    url, key = _load()
    return QdrantClient(url=url, api_key=key, cloud_inference=True, timeout=timeout)
