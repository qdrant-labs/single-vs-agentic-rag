"""Search tool for the benchmark questions.

    python -I bench_tool.py context <run>
    python -I bench_tool.py search <run> "<query>" [page]
    python -I bench_tool.py open <run> <post number>
    python -I bench_tool.py answer <run> <chunk ids, comma-separated> "<answer>"
    python -I bench_tool.py not_found <run>
"""
import sys
import urllib.parse
import urllib.request

BASE = "http://127.0.0.1:8770"


def main(argv):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if len(argv) < 2:
        print(__doc__)
        return 1
    cmd, run, rest = argv[0], argv[1], argv[2:]
    params = {"run": run}
    if cmd == "search":
        params["q"] = rest[0] if rest else ""
        params["page"] = rest[1] if len(rest) > 1 else "0"
    elif cmd == "open":
        params["post"] = rest[0] if rest else ""
    elif cmd == "answer":
        params["ids"] = rest[0] if rest else ""
        params["text"] = " ".join(rest[1:])
    elif cmd not in ("context", "not_found"):
        print(__doc__)
        return 1
    url = f"{BASE}/{cmd}?{urllib.parse.urlencode(params)}"
    print(urllib.request.urlopen(url, timeout=180).read().decode("utf-8"))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
