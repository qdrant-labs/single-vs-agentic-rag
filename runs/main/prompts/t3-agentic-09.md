You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- fd6e526f: In Oracle, does making a large varchar2 column the primary key slow a heap table compared with just putting a normal index on that column?
- 2b1157cb: I'm new to building apps for Google's phone OS and the official developer site has no clear reading order. What did one person use to get a guided overview before reading it?
- 98f38cc9: In bash, how can I make .* match all hidden files except . and .., and what exactly does the glob .??* match?
- 8eb3c121: I'm drawing a modelling diagram for a codebase that mixes classes with free-standing helper routines doing I/O. How could I show those routines without cluttering the picture?
- 10b8e9ab: Which build task should be used in Azure DevOps for a .NET Core 3.0 app hosted on Ubuntu?
- ef2865e5: Which pipeline prints only the grand total disk usage of a set of *.sql files, and which one lists directories sorted by size, largest first, in human-readable units?
- d02e4da5: Can I run a graphical app in Docker on a headless server by mounting the X11 libraries from a separate container through a volume?
- 55f2d94f: Why might a Unix system deliberately leave /usr/local out of root's PATH?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.