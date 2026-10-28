"""Dense search over the benchmark collection, for ground-truth checks only.

    RAG_BENCH_ENV_FILE=... python -I scripts/dense_search.py "<query>" [n]
"""
import pathlib
import sys

from qdrant_client import models

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from qdrant_conn import COLLECTION, MODEL, client  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = int(sys.argv[2]) if len(sys.argv) > 2 else 20
pts = client().query_points(COLLECTION, query=models.Document(text=sys.argv[1], model=MODEL), limit=n,
                            search_params=models.SearchParams(hnsw_ef=128),
                            with_payload=["post", "site", "text"]).points
for p in pts:
    print(f"[chunk {p.id}] (post {p.payload['post']}, {p.payload['site']}, score {p.score:.3f})\n{p.payload['text']}\n")
