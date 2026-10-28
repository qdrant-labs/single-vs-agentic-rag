You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 51d1261a: A site-to-site VPN tunnel on a Cisco ASA shows as up but passes no traffic. Which ASA software version resolved this for one user?
- fa5542f0: Why does GNU tr mangle UTF-8 characters, and what must a Perl one-liner add so tr/// with fullwidth letters in its source code works, given that -C alone does not help?
- 61b604e2: Can a child process change its parent's environment variables, and if I must alter a running process's environment anyway, which debugger sequence is suggested?
- f85451fa: I want agents' Cisco phones to auto-dial a customer list. What is this feature called, and which Cisco product is the cheaper, simpler option for it?
- 7be56528: My window manager doesn't see a timezone variable I exported in ~/.bashrc. Which file should I define it in instead, and which shells never read that file?
- 72f0e43f: On a cheap shared host my site sits behind an Apache add-on that blocks known attack patterns. Is relying on it alone a good security policy, and what did one admin prefer instead?
- f27dbfbe: Which driver module is needed to install Oracle Linux 6.4 on a ProLiant DL380e Gen8, and which boot options are added to the linuxefi line when installing CentOS 7 on a DL120 Gen9 with a B140i controller?
- f7a5d6fd: In a SQL Server availability group, how can I stop reporting-only accounts from ever logging into the current writable node even when their connection strings lack read-only intent?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.