"""Weak-retrieval signals for the single pass, for the gated-pipeline test.

    RAG_BENCH_ENV_FILE=... python -I scripts/gate_signals.py    # writes runs/main/gate_signals.json

Reruns each question's single-pass search exactly as bench_server.py did (question text,
top 10, hnsw_ef=128, rescoring) and keeps the scores, which the run log did not store.
Also runs the question through the local BM25 index (data/chunks_fts.sqlite, the same
1M chunks) for the dense-vs-sparse agreement signal. Checks that every rerun returns the
same top 10 the logged single-pass runs saw.
"""
import collections
import json
import pathlib
import re
import sqlite3
import sys

from qdrant_client import models

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from qdrant_conn import COLLECTION, MODEL, client  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
RUN = ROOT / "runs" / "main"
PARAMS = models.SearchParams(hnsw_ef=128, quantization=models.QuantizationSearchParams(rescore=True))

qs = json.load(open(ROOT / "data" / "questions.json", encoding="utf-8"))
assign = json.load(open(RUN / "assign.json"))
logged = collections.defaultdict(list)          # qid -> top-10 ids each single run was shown
for e in map(json.loads, open(RUN / "events.jsonl", encoding="utf-8")):
    if e.get("ev") == "context":
        logged[assign[e["run"]]["qid"]].append(e["ids"])

C = client(timeout=60)
fts = sqlite3.connect(ROOT / "data" / "chunks_fts.sqlite")
out, mismatch = {}, []
for q in qs:
    pts = C.query_points(COLLECTION, query=models.Document(text=q["question"], model=MODEL), limit=10,
                         search_params=PARAMS, with_payload=False).points
    dense = [(p.id, p.score) for p in pts]
    words = [w for w in re.findall(r"[A-Za-z0-9_.\-/]+", q["question"]) if len(w) > 1]
    match = " OR ".join('"' + w.replace('"', '') + '"' for w in words)
    bm25 = [r[0] for r in fts.execute("SELECT id FROM c WHERE c MATCH ? ORDER BY bm25(c) LIMIT 10", (match,))]
    ids = [i for i, _ in dense]
    if any(ids != seen for seen in logged[q["qid"]]):
        mismatch.append(q["qid"])
    out[q["qid"]] = {"dense": dense, "bm25": bm25}
json.dump(out, open(RUN / "gate_signals.json", "w"))
print(f"{len(out)} questions; logged single runs per question: "
      f"{collections.Counter(len(v) for v in logged.values())}; top-10 differs from a logged run: {len(mismatch)} {mismatch[:10]}")
