You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 09466f2c: To start a document database server in the background so it survives logout, what is the argument for using the server's own built-in backgrounding option over a shell wrapper that ignores hangups?
- 0c6c2128: kubectl says the server could not find the requested resource. What kubectl-to-cluster version rule should I check, and what are the fixes?
- 24813771: Is it supported to configure BFD on a virtual-template or dialer interface on Cisco IOS-XE 3S?
- 8c150194: How many key-derivation iterations does a KeePass database use by default, and what extra step makes a cloud-stored copy of the database harder to breach?
- b11ea3bc: On SQL Server 2008 R2 or 2012, how can I quickly check whether my application relies on features slated for removal?
- 2dc32dee: In Postgres, a partial index is ignored when the query has a big IN list. Which release removes this limitation, and what element limit applied before?
- 292a67ad: In my WPF app a base view model has one handler that picks the action from a string in the XAML. What problem arises if a child class must change just one action's behavior?
- 9d545c74: Can a database attached to a newer SQL Server release be moved back to an older release if I keep the same compatibility level?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.