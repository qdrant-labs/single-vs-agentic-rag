You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 90adcfd8: Besides provider documentation, what general way works to find out the attributes of any Terraform object you can refer to in an expression?
- a0bfcfab: In a code review dispute over assigning a comparison result to a boolean field like obj.NeedsChange, what small readability tweak was suggested as a compromise?
- 051eb018: How can I start a program automatically when CPU percent reaches a certain level on Windows?
- 936dacbd: What database design is recommended when 30 users each need full, private access to only their own data?
- 0fce3163: In SQL Server, how can I write decimal multiplication and division so the result's precision and scale stay predictable, and what formula gives the result scale of a division before it is capped?
- a17176e6: What distinguishes a VPN concentrator from a VPN gateway, given that the two terms are used interchangeably?
- dcda680b: When sending a for loop to a remote host over ssh, why do the loop variables come out empty if the command is in double quotes, and what can you do when the remote login shell is tcsh?
- fabb3efb: Why does piping grep into xargs dirname inside find -exec print a usage message for files that don't match, and how can bash make a shell function available to find -exec?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.