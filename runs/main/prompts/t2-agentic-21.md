You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 97aaaea7: How can you recover the public key of an AWS EC2 key pair by launching a temporary instance?
- 8ee95721: Which HTTP method is suggested as the simplest way to fire a non-RESTful action such as a reload, and what must the response metadata avoid when that method is used to propagate a signal?
- 7c4fa837: On a Debian-based system the man page for cp is missing, and other commands have no page either. Which dpkg config file edit restores the standard pages, and which man section holds POSIX descriptions of the other commands?
- 3e1965c7: Which GNU screen commands switch on background colour erase for a window and for the default of all new screens, and when did tmux implement that capability?
- 04fccff8: In the fish shell, how do I find and rerun an old command when I only remember part of it?
- a3cf294a: In a CircleCI 2.0 config, how do I make a private deploy key I uploaded in the dashboard usable inside a job?
- 97f232d6: Which gcc options produce annotated assembly to read when learning how code maps to machine instructions, and why are CPU opcode values not chosen arbitrarily?
- 91641965: A computer booting with no IP configured asks the network for an address. How can the server reply directly to it rather than shouting to everyone?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.