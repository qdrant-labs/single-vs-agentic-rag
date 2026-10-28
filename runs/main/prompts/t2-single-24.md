You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- bb2b3d0f: On a Debian-based system the man page for cp is missing, and other commands have no page either. Which dpkg config file edit restores the standard pages, and which man section holds POSIX descriptions of the other commands?
- 777db948: In a Declarative Jenkins pipeline, if one stage writes a value to a file with writeFile and a later stage reads it back with readFile, what limitation applies?
- dbf5353a: Is it supported to configure BFD on a virtual-template or dialer interface on Cisco IOS-XE 3S?
- 6e50848e: On a Cisco chassis switch with removable line cards, what global configuration command turns one card fully off instead of just restarting it?
- 4fc2fadc: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?
- 7e63fe5d: When sending a for loop to a remote host over ssh, why do the loop variables come out empty if the command is in double quotes, and what can you do when the remote login shell is tcsh?
- 15ef3304: Two causes of a MySQL server crashing: for oversized TEXT/BLOB data, which two my.cnf settings and values are recommended, and for a corrupt InnoDB data dictionary what is the only sure cleanup?
- 73dc2460: A tenant changed their apartment's network setup on a fiber line they had been told was capped at 100 down and 50 up. What speeds did they then measure?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.