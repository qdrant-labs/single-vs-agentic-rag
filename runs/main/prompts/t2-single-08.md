You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d7ee2ffe: How much signal loss does Plexiglas cause at 2.3GHz versus 5.25GHz?
- 570bfe8f: SSH to my VPS fails with "Server refused to allocate pty". What commands re-create the pty devices, and which command regenerates the Ubuntu initramfs where devpts gets mounted?
- 967838d9: My container builds keep re-downloading external binaries and libraries from outside sources on every run. What kind of tool can I host to store those dependencies locally, and which two popular ones have free open source editions?
- 2fb9ade2: On SQL Server 2008 R2 or 2012, how can I quickly check whether my application relies on features slated for removal?
- a2f14b23: In bash, how do I pass a wget user-agent option containing spaces from a variable correctly, and what is a safer alternative to eval for filling variables into a stored template string later?
- 3c904455: My web server log shows GET requests mentioning cmd.exe and System.Net.WebClient that returned 404. What do they indicate, and why do people send requests for pages that don't exist?
- 24ea274a: To avoid programming by coincidence, how much new code should I add between test runs, according to the advice on shortening the edit/compile/test cycle?
- bc6d3ada: Some accounts on my site get activated even though the person never clicked the confirmation link I emailed. What could cause that, and how can I guard against it?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.