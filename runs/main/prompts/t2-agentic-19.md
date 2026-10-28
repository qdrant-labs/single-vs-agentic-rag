You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d55d131f: In SQL Server, what error occurs when a distributed query is run against a loopback linked server from within a distributed transaction?
- cd517b3f: Why is the MAC address bb:bb:bb:bb:bb:bb treated as a non-unicast address?
- b69f789b: Why would adding a random per-user value before hashing not have stopped a big social network's leaked password hashes from being cracked, and what should they have used?
- 7f7a3847: In Vim in a terminal, how do I map Ctrl-S to save, and what does Ctrl-S do at the terminal level that can interfere, and which key undoes it?
- 9aa687b5: My container builds keep re-downloading external binaries and libraries from outside sources on every run. What kind of tool can I host to store those dependencies locally, and which two popular ones have free open source editions?
- 42821e2e: Which build task should be used in Azure DevOps for a .NET Core 3.0 app hosted on Ubuntu?
- 5b3ac636: What habits help design patterns emerge pragmatically instead of being forced onto code, and what is the main lasting benefit of knowing pattern names such as Strategy or Builder?
- d245d297: In SQL Server, what permission benefit is lost by spreading related code across separate databases, and what kind of data requirement forces tables to share one database?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.