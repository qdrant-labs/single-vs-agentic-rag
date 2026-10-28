You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 7ad86beb: Where can I find open scripts for hardening Enterprise Linux servers to a US Defense Department security guideline, including one that builds a pre-hardened installer image?
- 2e8d1e03: To decouple CI tooling data from servers with an immutable architecture, which tools are suggested for static analysis, artifact storage, base images and deployment?
- f14dee34: Which pipeline prints only the grand total disk usage of a set of *.sql files, and which one lists directories sorted by size, largest first, in human-readable units?
- ddd5014e: What workaround is suggested when a new RDS MySQL 8.0.16 instance has an empty ST_SPATIAL_REFERENCE_SYSTEMS table?
- 33ffef04: How do I let a parameter choose between different multi-column sort orders in a SQL Server ORDER BY, and why does it fail with a conversion error when the sorted columns have different data types?
- 5327543e: Why do many hardware controllers, such as wireless adapters or GPUs, need their firmware supplied again at every power-on, and which host component does that loading?
- f96f9515: I'm drawing a modelling diagram for a codebase that mixes classes with free-standing helper routines doing I/O. How could I show those routines without cluttering the picture?
- f8d5d713: In which ksh93 release did the exec {fd}</file style of redirection become available, and what problem with hard-coded descriptors like exec 4< does it avoid?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.