You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 520a6f3c: Is a SHA-1 hash of a string always the same, or can different implementations give different results?
- 59eb4e75: On a Debian-based system the man page for cp is missing, and other commands have no page either. Which dpkg config file edit restores the standard pages, and which man section holds POSIX descriptions of the other commands?
- 27c4c1c0: Two distros share one swap partition. What must be done to the swap space at boot for sharing to work, and why is hibernating one install and then booting the other dangerous?
- 1929f779: Why do exported variables from a shell script vanish after I run it, and what file permission difference is there between running it directly and passing its path to an interpreter?
- ef640073: On a Cisco chassis switch with removable line cards, what global configuration command turns one card fully off instead of just restarting it?
- ee474b52: When building a writable snapshot overlay on a read-only loop device so LVM will activate it, how do you stop LVM complaining about duplicate PVs, and how can you check how full the overlay is?
- 555f2df9: When I poll a router with a command-line walk tool on Ubuntu, I only see long dotted numeric identifiers instead of readable names. How do I fix that?
- bb536127: For an HP P410 RAID with Samsung 830 SSDs on Debian 6.0, which change gives the greatest performance improvement?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.