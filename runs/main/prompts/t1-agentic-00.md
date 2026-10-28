You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 0884d1d6: How do I stop Outlook repeatedly prompting for credentials over RPC over HTTPS, given Remember my Password doesn't cover the front-end proxy server?
- bb9f29c4: A process protected with nohup still dies when I log out and logind.conf has KillUserProcesses=yes. What command is the workaround?
- ee6cfe68: To make a 2008-era Microsoft relational database redundant, what approach is recommended over delayed copying, failover clusters or hypervisor HA, and how many servers does it need?
- 3a6afc41: Is it safe to tell everyone which password hash my site uses if I publish its source code, and what alternative is suggested if the site owner is uneasy about public code?
- 603b9119: In bash, how can I make .* match all hidden files except . and .., and what exactly does the glob .??* match?
- 1dea0dbf: My window manager doesn't see a timezone variable I exported in ~/.bashrc. Which file should I define it in instead, and which shells never read that file?
- 67306532: To make a bootable USB copy of a running Linux system, which command copies the root filesystem without crossing mount points, and why is running dd on a mounted live filesystem risky, and what gives a consistent copy instead?
- dd74d34b: How can rsync keep deleted or overwritten files in a separate directory instead of discarding them, and how can I delete from one directory every file that exists at the same relative path in another?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.