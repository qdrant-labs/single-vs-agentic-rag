You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 29bd64c3: I applied IP-based packet filter rules to a switch port carrying several tagged VLANs and nothing is filtered. Why is that, and where do the rules belong?
- 978cf430: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?
- 37406716: In Packet Tracer with a serial DCE cable between two routers, which router becomes the DCE end and how can I identify it on the link?
- d20ee255: Ctrl-C would not stop pppd running in non-detached mode from a shell script. What turned out to be the cause?
- 416b109a: Pulse Secure's client UI on Ubuntu 22.04 can't download its Chromium Embedded Framework. Which script and argument install it manually, and how do I verify it?
- d810ea50: I want to see which of my SQL Server databases are busiest right now. Which built-in view could I query, and what session id threshold excludes internal sessions?
- d54d1b4c: After upgrading my Linux desktop environment, opening a link from another app no longer switches me to the workspace where my browser window lives. Which window behavior setting restores that?
- 86c58e21: In SQL Server, how can I write decimal multiplication and division so the result's precision and scale stay predictable, and what formula gives the result scale of a division before it is capped?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.