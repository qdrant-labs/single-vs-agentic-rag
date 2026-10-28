"""Tool server for both pipelines. Sub-agents talk to it through scripts/bench_tool.py.

Each run id maps to (question, pipeline, trial) in runs/<name>/assign.json; only the server
knows which question and which pipeline a run belongs to.

single  : `context <run>` returns the top 10 chunks for the question text (one dense search,
          chosen by the harness, not the model). Allowed once. Then `answer` or `not_found`.
agentic : `search <run> "<query>" [page]` (10 per page, depth 50) and `open <run> <post>`
          (the full answer the chunk came from), at most BUDGET search/open calls, then
          `answer` or `not_found`.
Both    : `answer <run> <chunk ids, comma-separated> "<answer text>"` or `not_found <run>`.

Every Qdrant call is timed. Events go to runs/<name>/events.jsonl and one row per finished
run to runs/<name>/results.jsonl.

    RAG_BENCH_ENV_FILE=... python -I scripts/bench_server.py <run name>
"""
import json
import pathlib
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from qdrant_client import models

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from qdrant_conn import COLLECTION, MODEL, client  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
NAME = sys.argv[1]
RUN_DIR = ROOT / "runs" / NAME
ASSIGN = json.load(open(RUN_DIR / "assign.json", encoding="utf-8"))
QFILE = pathlib.Path(__import__("os").environ.get("BENCH_QUESTIONS", ROOT / "data" / "questions.json"))
QUESTIONS = {q["qid"]: q for q in json.load(open(QFILE, encoding="utf-8"))}
TOP_K, PAGE, DEPTH, BUDGET = 10, 10, 50, 6
SEARCH_PARAMS = models.SearchParams(hnsw_ef=128, quantization=models.QuantizationSearchParams(rescore=True))

C = client(timeout=60)
LOCK = threading.Lock()          # guards STATE and the log files, not the Qdrant calls
STATE = {}


def log(row):
    with open(RUN_DIR / "events.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")


def search(text, limit):
    t0 = time.perf_counter()
    res = C.query_points(COLLECTION, query=models.Document(text=text, model=MODEL), limit=limit,
                         search_params=SEARCH_PARAMS, with_payload=["site", "thread", "post", "title", "text"])
    return res.points, (time.perf_counter() - t0) * 1000


def fmt(points):
    return "\n\n".join(f"[chunk {p.id}] (post {p.payload['post']}, {p.payload['site']})\n{p.payload['text']}"
                       for p in points)


def state(run):
    if run not in STATE:
        STATE[run] = {"calls": 0, "searches": 0, "opens": 0, "qdrant_ms": [], "shown": set(),
                      "queries": [], "context": False, "done": False, "t_first": None, "rankings": {}}
    return STATE[run]


def finish(run, kind, ids=(), text=""):
    a, s = ASSIGN[run], state(run)
    s["done"] = True
    t_end = time.time()
    row = {"run": run, "qid": a["qid"], "pipeline": a["pipeline"], "trial": a["trial"], "batch": a["batch"],
           "final": kind, "answer": text, "cited": list(ids), "cited_shown": all(i in s["shown"] for i in ids),
           "calls": s["calls"], "searches": s["searches"], "opens": s["opens"], "queries": s["queries"],
           "shown": sorted(s["shown"]), "qdrant_ms": s["qdrant_ms"],
           "t_first": s["t_first"], "t_end": t_end,
           "e2e_s": (t_end - s["t_first"]) if s["t_first"] else None}
    with open(RUN_DIR / "results.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(row) + "\n")
    return "Recorded."


def handle(path, p):
    run = p.get("run", "")
    if run not in ASSIGN:
        return "Unknown run id."
    a = ASSIGN[run]
    with LOCK:
        s = state(run)
        if s["done"]:
            return "This question is finished. Move on to the next one."
        if s["t_first"] is None:
            s["t_first"] = time.time()
    q = QUESTIONS[a["qid"]]
    if path == "/context":
        if a["pipeline"] != "single":
            return "Use search and open for this question."
        if s["context"]:
            return "Context was already given for this question. Answer or record not_found."
        pts, ms = search(q["question"], TOP_K)
        with LOCK:
            s["context"], s["calls"] = True, s["calls"] + 1
            s["searches"] += 1
            s["qdrant_ms"].append(ms)
            s["shown"] |= {p.id for p in pts}
            s["queries"].append(q["question"])
        log({"t": time.time(), "run": run, "ev": "context", "ms": ms, "ids": [p.id for p in pts]})
        return fmt(pts)
    if path in ("/search", "/open"):
        if a["pipeline"] != "agentic":
            return "This question allows only context, then answer or not_found."
        if s["calls"] >= BUDGET:
            with LOCK:
                finish(run, "budget")
            return "Search budget used up for this question. Move on to the next one."
    if path == "/search":
        query = p.get("q", "").strip()
        page = max(0, int(p.get("page", "0") or 0))
        if not query:
            return "Empty query."
        if query not in s["rankings"]:
            pts, ms = search(query, DEPTH)
            s["rankings"][query] = pts
        else:
            ms = 0.0
        hits = s["rankings"][query][page * PAGE:(page + 1) * PAGE]
        with LOCK:
            s["calls"] += 1
            s["searches"] += 1
            s["qdrant_ms"].append(ms)
            s["shown"] |= {h.id for h in hits}
            s["queries"].append(query)
        log({"t": time.time(), "run": run, "ev": "search", "page": page, "ms": ms, "ids": [h.id for h in hits]})
        return fmt(hits) if hits else "No more results for this query."
    if path == "/open":
        try:
            post = int(p.get("post", ""))
        except ValueError:
            return "Give a post number."
        t0 = time.perf_counter()
        pts, _ = C.scroll(COLLECTION, scroll_filter=models.Filter(must=[models.FieldCondition(
            key="post", match=models.MatchValue(value=post))]), limit=64, with_payload=["post", "chunk", "text", "site"])
        ms = (time.perf_counter() - t0) * 1000
        pts = sorted(pts, key=lambda x: x.payload["chunk"])
        with LOCK:
            s["calls"] += 1
            s["opens"] += 1
            s["qdrant_ms"].append(ms)
            s["shown"] |= {x.id for x in pts}
        log({"t": time.time(), "run": run, "ev": "open", "post": post, "ms": ms, "ids": [x.id for x in pts]})
        return fmt(pts) if pts else "No post with that number."
    if path in ("/answer", "/not_found"):      # answers must come from retrieved text
        if a["pipeline"] == "single" and not s["context"]:
            return "Run the context command for this question first."
        if a["pipeline"] == "agentic" and s["searches"] + s["opens"] == 0:
            return "Search at least once before answering this question."
    if path == "/answer":
        ids = [int(x) for x in p.get("ids", "").replace(" ", "").split(",") if x.strip().isdigit()]
        with LOCK:
            return finish(run, "answer", ids, p.get("text", ""))
    if path == "/not_found":
        with LOCK:
            return finish(run, "not_found")
    return "Unknown command."


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        u = urlparse(self.path)
        try:
            out = handle(u.path, {k: v[0] for k, v in parse_qs(u.query).items()})
        except Exception as e:  # report, do not crash the server
            out = f"Server error: {type(e).__name__}. Try the same command again."
            log({"t": time.time(), "ev": "error", "path": u.path, "error": repr(e)[:300]})
        body = out.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"bench server ready on 127.0.0.1:8770 ({NAME}, {len(ASSIGN)} runs)", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8770), Handler).serve_forever()
