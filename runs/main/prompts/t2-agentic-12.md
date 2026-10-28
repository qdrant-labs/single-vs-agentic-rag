You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 75e874fd: Which pipeline prints only the grand total disk usage of a set of *.sql files, and which one lists directories sorted by size, largest first, in human-readable units?
- 6c5efd48: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?
- dce0c36e: Since which SQL Server version is the built-in Windows Administrators group not made sysadmin by default, and if no sysadmin login remains, does the Dedicated Administrator Connection let you recover one?
- 861cad8b: People tell me to code against abstractions, but making a separate abstract type for every class seems absurd. In what broader sense can that advice be applied beyond language keywords?
- 91062f3f: In a SQL Server availability group, how can I stop reporting-only accounts from ever logging into the current writable node even when their connection strings lack read-only intent?
- 0478418d: In bash, how do I pass a wget user-agent option containing spaces from a variable correctly, and what is a safer alternative to eval for filling variables into a stored template string later?
- 3dd71fe2: On a cheap shared host my site sits behind an Apache add-on that blocks known attack patterns. Is relying on it alone a good security policy, and what did one admin prefer instead?
- b2ff937b: How do I concatenate many files without exceeding the command line length limit, and what constraint applies to files when using device mapper to build a virtual concatenated file?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.