You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 42620a56: I administer Microsoft's database server from an Apple laptop, where the old GUI tracing tool doesn't run. Is there an open source script that finds the most resource-hungry queries from the plan cache without starting a trace?
- c9eb9e17: How do I stop Outlook repeatedly prompting for credentials over RPC over HTTPS, given Remember my Password doesn't cover the front-end proxy server?
- 67778a8e: What free toolset is recommended on Linux for collecting and reporting NetFlow data, and which free collector runs on Windows but needs recompiling because its supplied build is limited?
- 8164148d: When building a writable snapshot overlay on a read-only loop device so LVM will activate it, how do you stop LVM complaining about duplicate PVs, and how can you check how full the overlay is?
- de9ffc1c: What distinguishes a VPN concentrator from a VPN gateway, given that the two terms are used interchangeably?
- 928b537f: I keep contacts for a small church group in one wide table with a column per detail. Should I break out separate tables for things like addresses and churches?
- 00b0528a: I have an executable script written in the classic Unix pattern-scanning language, and flags like -h are swallowed by the interpreter. With GNU coreutils 8.30 or newer, what shebang passes them through to the script?
- aea53146: On a pair of Cisco Nexus switches sharing a multi-chassis port channel, must the trunk's allowed list of Layer 2 segments match on both switches to avoid the channel being suspended?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.