You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 256e2e89: In a SQL Server deadlock graph, an IX lock request is blocked by an SIU page lock after a SELECT with UPDLOCK. What turns the IU page lock into SIU?
- ceb89bc4: My container builds keep re-downloading external binaries and libraries from outside sources on every run. What kind of tool can I host to store those dependencies locally, and which two popular ones have free open source editions?
- 27fbc748: In SSRS, the page setup print options don't change my report's orientation. What do I set in BIDS instead?
- 010e9458: Two causes of a MySQL server crashing: for oversized TEXT/BLOB data, which two my.cnf settings and values are recommended, and for a corrupt InnoDB data dictionary what is the only sure cleanup?
- 589353e0: In the fish shell, how do I find and rerun an old command when I only remember part of it?
- 7488e03e: Besides encrypting traffic, what does a CA-signed web server certificate establish, and which certificate should an ordinary site that is not a bank buy?
- 1bf60620: What database design is recommended when 30 users each need full, private access to only their own data?
- 91018330: Which standard number was the LLDP-MED extension published under, and by which organization and when?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.