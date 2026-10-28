"""Build the ~1M-chunk corpus from the Stack Exchange dumps.

    python -I scripts/build_corpus.py extract   # Posts.xml + PostLinks.xml per site
    python -I scripts/build_corpus.py parse     # answers + threads + links per site
    python -I scripts/build_corpus.py chunk     # chunks.jsonl, deterministic

Rules (fixed before any question exists):
- an answer is kept if it is accepted or has score >= 1, and has >= 80 characters of text
- HTML is reduced to text; code blocks keep their text
- each answer is split into chunks of at most 500 characters on paragraph, then sentence,
  then word boundaries; every chunk is prefixed with its question title
- point ids are assigned in a fixed order (site, thread id, answer id, chunk index)

Inputs are read from data/raw/*.7z (untrusted downloads); outputs go to data/.
"""
import html
import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parent.parent
RAW, EXT, OUT = ROOT / "data" / "raw", ROOT / "data" / "extracted", ROOT / "data"
SITES = ["serverfault.com", "unix.stackexchange.com", "softwareengineering.stackexchange.com",
         "dba.stackexchange.com", "security.stackexchange.com",
         "networkengineering.stackexchange.com", "devops.stackexchange.com"]
MAX_CHARS, MIN_CHARS = 500, 80


def short(site):
    return site.replace(".stackexchange.com", "").replace(".com", "")


class Text(HTMLParser):
    BREAK = {"p", "br", "li", "pre", "h1", "h2", "h3", "h4", "blockquote", "tr", "div"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag in self.BREAK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BREAK:
            self.out.append("\n")

    def handle_data(self, data):
        self.out.append(data)


def to_text(body):
    p = Text()
    p.feed(body or "")
    text = html.unescape("".join(p.out))
    text = re.sub(r"[ \t]+", " ", text)
    return re.sub(r"\n\s*\n+", "\n\n", text).strip()


def split(text):
    """Chunks of at most MAX_CHARS: paragraphs first, then sentences, then words."""
    pieces = []
    for para in re.split(r"\n\s*\n", text):
        para = para.strip()
        if not para:
            continue
        if len(para) <= MAX_CHARS:
            pieces.append(para)
            continue
        for sent in re.split(r"(?<=[.!?])\s+", para):
            while len(sent) > MAX_CHARS:
                cut = sent.rfind(" ", 0, MAX_CHARS)
                cut = cut if cut > MAX_CHARS // 2 else MAX_CHARS
                pieces.append(sent[:cut].strip())
                sent = sent[cut:].strip()
            if sent:
                pieces.append(sent)
    chunks, cur = [], ""
    for p in pieces:
        if cur and len(cur) + 1 + len(p) > MAX_CHARS:
            chunks.append(cur)
            cur = p
        else:
            cur = f"{cur}\n{p}" if cur else p
    if cur:
        chunks.append(cur)
    return chunks


def extract():
    import py7zr
    for site in SITES:
        dest = EXT / short(site)
        if (dest / "Posts.xml").exists() and (dest / "PostLinks.xml").exists():
            continue
        if not (RAW / f"{site}.7z").exists():
            print("not downloaded yet, skipping:", site, flush=True)
            continue
        dest.mkdir(parents=True, exist_ok=True)
        with py7zr.SevenZipFile(RAW / f"{site}.7z", "r") as z:
            names = [n for n in z.getnames() if n.split("/")[-1] in ("Posts.xml", "PostLinks.xml")]
            z.extract(path=dest, targets=names)
        print("extracted", site, names, flush=True)


def parse():
    for site in SITES:
        s = short(site)
        dest = EXT / s
        out = OUT / "parsed" / s
        out.mkdir(parents=True, exist_ok=True)
        if (out / "answers.jsonl").exists():
            continue
        if not (dest / "Posts.xml").exists():
            print("not extracted yet, skipping:", site, flush=True)
            continue
        threads, answers = {}, []
        for _, el in ET.iterparse(dest / "Posts.xml", events=("end",)):
            if el.tag != "row":
                continue
            a = el.attrib
            if a.get("PostTypeId") == "1":
                threads[a["Id"]] = {"title": html.unescape(a.get("Title", "")), "tags": a.get("Tags", ""),
                                    "accepted": a.get("AcceptedAnswerId"), "score": int(a.get("Score", 0))}
            elif a.get("PostTypeId") == "2":
                answers.append({"id": a["Id"], "parent": a.get("ParentId"), "score": int(a.get("Score", 0)),
                                "body": a.get("Body", "")})
            el.clear()
        kept = 0
        with open(out / "answers.jsonl", "w", encoding="utf-8") as f:
            for a in answers:
                t = threads.get(a["parent"])
                if not t:
                    continue
                accepted = t["accepted"] == a["id"]
                if not (accepted or a["score"] >= 1):
                    continue
                text = to_text(a["body"])
                if len(text) < MIN_CHARS:
                    continue
                f.write(json.dumps({"site": s, "thread": int(a["parent"]), "post": int(a["id"]),
                                    "score": a["score"], "accepted": accepted, "title": t["title"],
                                    "tags": t["tags"], "text": text}) + "\n")
                kept += 1
        json.dump({k: v for k, v in threads.items()}, open(out / "threads.json", "w", encoding="utf-8"))
        links = []
        for _, el in ET.iterparse(dest / "PostLinks.xml", events=("end",)):
            if el.tag == "row":
                links.append([int(el.attrib["PostId"]), int(el.attrib["RelatedPostId"]), int(el.attrib["LinkTypeId"])])
            el.clear()
        json.dump(links, open(out / "links.json", "w"))
        print(f"{s}: threads {len(threads)}, answers {len(answers)}, kept {kept}, links {len(links)}", flush=True)


def chunk():
    n_ans = n_chunks = 0
    with open(OUT / "chunks_all.jsonl", "w", encoding="utf-8") as f:
        for site in SITES:
            s = short(site)
            rows = [json.loads(l) for l in open(OUT / "parsed" / s / "answers.jsonl", encoding="utf-8")]
            rows.sort(key=lambda r: (r["thread"], r["post"]))
            for r in rows:
                parts = split(r["text"])
                n_ans += 1
                for i, p in enumerate(parts):
                    f.write(json.dumps({"site": s, "thread": r["thread"], "post": r["post"], "chunk": i,
                                        "n_chunks": len(parts), "score": r["score"], "accepted": r["accepted"],
                                        "title": r["title"], "text": f"{r['title']}\n{p}"}) + "\n")
                    n_chunks += 1
    print(f"answers {n_ans}, chunks {n_chunks}")


if __name__ == "__main__":
    {"extract": extract, "parse": parse, "chunk": chunk}[sys.argv[1]]()
