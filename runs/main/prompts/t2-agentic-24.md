You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- c3c1ac97: How much in Azure credits could a startup qualify for through Microsoft's BizSpark programme to host an application?
- a99ff8ef: Using only its first line, how can I make a library script meant only for sourcing print a notice if someone executes it directly, and what decides which interpreter runs a script when no interpreter is named on the command line, given the file extension does not?
- e9c54875: How much signal loss does Plexiglas cause at 2.3GHz versus 5.25GHz?
- d5333ed5: What database design is recommended when 30 users each need full, private access to only their own data?
- 51307004: After renaming my Windows server, the Oracle listener won't start. How do I find the file to edit and what do I change?
- 5835b5a9: I'm considering enabling Google's experimental faster web transport protocol on my TLS site. Which known attack on compressed headers and cookies is the security concern?
- eb8a033e: In a SQL Server deadlock graph, an IX lock request is blocked by an SIU page lock after a SELECT with UPDLOCK. What turns the IU page lock into SIU?
- 9a78a4da: Two distros share one swap partition. What must be done to the swap space at boot for sharing to work, and why is hibernating one install and then booting the other dangerous?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.