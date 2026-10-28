You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 5779e572: I want to see which of my SQL Server databases are busiest right now. Which built-in view could I query, and what session id threshold excludes internal sessions?
- 59b370f8: Since patching my servers against the speculative-execution CPU bugs, some boxes slowed a lot and others not at all. What kind of workload is hit hardest, and why?
- b58bf765: In which ksh93 release did the exec {fd}</file style of redirection become available, and what problem with hard-coded descriptors like exec 4< does it avoid?
- c707a9dd: Is a SHA-1 hash of a string always the same, or can different implementations give different results?
- 9d583f7f: I'm drawing a modelling diagram for a codebase that mixes classes with free-standing helper routines doing I/O. How could I show those routines without cluttering the picture?
- 8bf18199: Why would adding a random per-user value before hashing not have stopped a big social network's leaked password hashes from being cracked, and what should they have used?
- 53a9e3e6: I'm considering enabling Google's experimental faster web transport protocol on my TLS site. Which known attack on compressed headers and cookies is the security concern?
- b8c3b212: Besides avoiding rounding on every query, what index-related benefit comes from storing timestamps with lower precision in PostgreSQL?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.