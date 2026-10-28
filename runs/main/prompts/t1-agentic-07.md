You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 8fc5f6be: How does Sonatype Nexus 3 Pro provide high availability for the artifact repository, and what are its mechanisms collectively called?
- 587e8b0a: I have an executable script written in the classic Unix pattern-scanning language, and flags like -h are swallowed by the interpreter. With GNU coreutils 8.30 or newer, what shebang passes them through to the script?
- 4d3de972: I'm new to building apps for Google's phone OS and the official developer site has no clear reading order. What did one person use to get a guided overview before reading it?
- 6e959bd4: What ASA feature allows handling multiple VLANs with the same subnet behind a single ASA?
- 7fc57ac0: Can a database attached to a newer SQL Server release be moved back to an older release if I keep the same compatibility level?
- 7975003a: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?
- b650e883: Which kernel release did a brand-new Radeon HD 6450 need for full resolution on Fedora, and if the boot then freezes after X was reconfigured, which file should be deleted and which log checked?
- 7df8f0c8: Our servers sit behind a device that spreads incoming requests, and it is also their default gateway. How can server-to-server traffic avoid passing through it?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.