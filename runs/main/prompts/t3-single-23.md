You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d2b7a818: Which GNU screen commands switch on background colour erase for a window and for the default of all new screens, and when did tmux implement that capability?
- 2ab65eee: Apache writes its files into a private, hash-named directory under /tmp. What setting causes that, and how can I change it for Apache's unit without editing the package-supplied unit file?
- cd2fc1e4: Some accounts on my site get activated even though the person never clicked the confirmation link I emailed. What could cause that, and how can I guard against it?
- a50f69bb: How can a cron job reshuffle a word-of-the-day data file each day so that the script only needs to pick the first line?
- 29e4e317: Should a command's --help usage message go to stderr or stdout, and where should the usage message for an invalid option go?
- 2d73c94a: Why might a Unix system deliberately leave /usr/local out of root's PATH?
- 1b8a1cc8: I granted a login the server-wide right to run bulk file loads, but it still can't load rows into my target database in SQL Server. What other permission does it need there?
- d88b22a7: How can I build a Git commit history from successive snapshots of a code base, setting the author name and date on each imported commit?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.