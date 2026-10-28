"""Local keyword (BM25) search over exactly the indexed chunks, for ground-truth checks.

    python -I scripts/kw_index.py build                 # data/chunks_fts.sqlite from chunks.jsonl
    python -I scripts/kw_index.py search "<terms>" [n]  # top n by SQLite FTS5 bm25()

Used only by verifiers to confirm that an "unanswerable" question has no answer in the
index. The benchmark pipelines never see it.
"""
import json
import pathlib
import re
import sqlite3
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "chunks_fts.sqlite"


def build():
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.execute("CREATE VIRTUAL TABLE c USING fts5(text, id UNINDEXED, post UNINDEXED, site UNINDEXED)")
    rows = []
    for line in open(ROOT / "data" / "chunks.jsonl", encoding="utf-8"):
        r = json.loads(line)
        rows.append((r["text"], r["id"], r["post"], r["site"]))
        if len(rows) == 50_000:
            con.executemany("INSERT INTO c VALUES (?,?,?,?)", rows)
            rows = []
    if rows:
        con.executemany("INSERT INTO c VALUES (?,?,?,?)", rows)
    con.commit()
    print("indexed", con.execute("SELECT count(*) FROM c").fetchone()[0])


def search(terms, n=20):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    words = [w for w in re.findall(r"[A-Za-z0-9_.\-/]+", terms) if len(w) > 1]
    if not words:
        print("No search terms.")
        return
    q = " OR ".join('"' + w.replace('"', '') + '"' for w in words)
    con = sqlite3.connect(DB)
    rows = con.execute("SELECT id, post, site, text FROM c WHERE c MATCH ? ORDER BY bm25(c) LIMIT ?", (q, n)).fetchall()
    for i, post, site, text in rows:
        print(f"[chunk {i}] (post {post}, {site})\n{text}\n")
    if not rows:
        print("No matches.")


if __name__ == "__main__":
    if sys.argv[1] == "build":
        build()
    else:
        search(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 20)
