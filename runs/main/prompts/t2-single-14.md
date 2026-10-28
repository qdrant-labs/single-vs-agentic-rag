You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- b5ea33ce: In the one-line form if [ "a" == "a" ] ; then echo "true" ; fi, what are if and then technically in the shell, and which comparison operator is more portable than ==?
- 47f1814e: How do you fix COPY or rename failures when Nginx with an https frontend proxies WebDAV or SVN to an internal Apache over http?
- a3dfc1e9: Why do many web API designers still put the release number in the endpoint path despite purists' objections?
- 995cbc9c: How can a cron job reshuffle a word-of-the-day data file each day so that the script only needs to pick the first line?
- 4cde6481: In Vim in a terminal, how do I map Ctrl-S to save, and what does Ctrl-S do at the terminal level that can interfere, and which key undoes it?
- 3debd01e: My window manager doesn't see a timezone variable I exported in ~/.bashrc. Which file should I define it in instead, and which shells never read that file?
- ca2eb58a: How can I build a Git commit history from successive snapshots of a code base, setting the author name and date on each imported commit?
- 0894202b: I have an executable script written in the classic Unix pattern-scanning language, and flags like -h are swallowed by the interpreter. With GNU coreutils 8.30 or newer, what shebang passes them through to the script?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.