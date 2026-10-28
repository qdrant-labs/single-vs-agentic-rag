You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- bee67961: Why do many hardware controllers, such as wireless adapters or GPUs, need their firmware supplied again at every power-on, and which host component does that loading?
- 20ed8dcc: Why might a Unix system deliberately leave /usr/local out of root's PATH?
- 9382715a: What tool can be used to pause or suspend a KVM guest without virsh and libvirtd?
- 7093e19d: Which standard number was the LLDP-MED extension published under, and by which organization and when?
- 52ff119f: On Ubuntu, which package and command let me percent-encode a local path in a shell script so I can build a link starting with the file scheme?
- f44be388: My web server log shows GET requests mentioning cmd.exe and System.Net.WebClient that returned 404. What do they indicate, and why do people send requests for pages that don't exist?
- ef5d3424: In SSRS, the page setup print options don't change my report's orientation. What do I set in BIDS instead?
- 8ec70658: For Merkle-Damgard hashes like SHA-1, why does revealing h(P+B) give an attacker no extra information beyond h(P)?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.