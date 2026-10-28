You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 95b0e4ba: On a mounted NTFS volume with a recent ntfs-3g, which extended attribute can I read with getfattr to get a file's creation time?
- c73e24a2: A MySQL query filters on a very lopsided col1 = 1, adds a date range and LIKE on col2, and orders by date DESC with a small LIMIT. What single composite index is suggested on InnoDB?
- d0676b82: Ctrl-C would not stop pppd running in non-detached mode from a shell script. What turned out to be the cause?
- 2be624f9: Should a command's --help usage message go to stderr or stdout, and where should the usage message for an invalid option go?
- 8bad716a: How can users change their password without re-encrypting all their data, and if the key comes from a passphrase via PBKDF2 for an encrypt-then-MAC scheme, how many bits are derived and how are they used?
- 06884842: Is it supported to configure BFD on a virtual-template or dialer interface on Cisco IOS-XE 3S?
- e9f5eef7: For Merkle-Damgard hashes like SHA-1, why does revealing h(P+B) give an attacker no extra information beyond h(P)?
- deec6a7a: When is it worth issuing a new CSRF token within a session, rather than a new one for every form request?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.