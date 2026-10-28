You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 9b1dbe70: I'm designing storage for a chat bot's access rights, where users can have rights per channel and also globally. How should I lay out the tables?
- 89b21bed: To make a 2008-era Microsoft relational database redundant, what approach is recommended over delayed copying, failover clusters or hypervisor HA, and how many servers does it need?
- 8ad6bcbd: In the one-line form if [ "a" == "a" ] ; then echo "true" ; fi, what are if and then technically in the shell, and which comparison operator is more portable than ==?
- 636e810f: When a class only supports a single observer registered after construction, how should that limit be handled so allowing multiple observers later changes only the implementation?
- c30b8f95: Under what terms may the text of the GNU General Public License itself be copied and distributed?
- e49e382c: Where should a disk partition start to get roughly 70 MB/s writes instead of 29 MB/s, and in which kernel version did the log-structured NILFS2 filesystem become available?
- bf272b96: Which weakness of SHA-2 is the reason PBKDF2 is often built on HMAC, and how far does repeated iteration shrink the hash space of a 256-bit hash?
- 3f303274: A colleague says that managing our deployments through pull requests in a repository means we've adopted the whole cultural philosophy of joining development and operations. Is that right?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.