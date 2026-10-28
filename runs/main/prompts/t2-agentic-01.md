You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 178b49e3: What GitHub practices did one company adopt for ISO27001 certification, without moving to GitHub Enterprise?
- 3f4eaee3: When a class only supports a single observer registered after construction, how should that limit be handled so allowing multiple observers later changes only the implementation?
- 8d2f5389: Processing an SSAS Tabular model attached to an Analysis Services instance fails on impersonation. Which ImpersonationMode value is not supported for such databases?
- 7ba8b443: What is the difference between nscd and sssd, and should both run at the same time?
- 9fa8752a: A host answers telnet fine, but an openssl TLS connection to it fails with "No route to host". The name has both A and AAAA records. What is the likely cause?
- a4b5824f: Why must a load balancer rewrite the IP address in the node's response before forwarding it to the client?
- 29c1e7aa: Which kernel release did a brand-new Radeon HD 6450 need for full resolution on Fedora, and if the boot then freezes after X was reconfigured, which file should be deleted and which log checked?
- 6c87aa4f: How do you fix COPY or rename failures when Nginx with an https frontend proxies WebDAV or SVN to an internal Apache over http?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.