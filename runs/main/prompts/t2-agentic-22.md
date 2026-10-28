You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 81b4b373: How can I start a program automatically when CPU percent reaches a certain level on Windows?
- 36243e32: What is the earliest citation found for the term "rings" in computer protection domains, and who wrote it?
- 5e0925b9: Which driver module is needed to install Oracle Linux 6.4 on a ProLiant DL380e Gen8, and which boot options are added to the linuxefi line when installing CentOS 7 on a DL120 Gen9 with a B140i controller?
- 1084eadd: How does Sonatype Nexus 3 Pro provide high availability for the artifact repository, and what are its mechanisms collectively called?
- 6ecceb4d: If I can't use Let's Encrypt as my certificate authority, which ACME challenge types can Ansible's acme_certificate module handle?
- d9985aa0: On a Junos switch, one access port faces a customer who sends tagged frames. How can I map the customer's VLANs 41-42 into one provider VLAN and 51-52 into another on that single port?
- f271b20b: What is the term for a really big source code commit or patch that is so large no one can review it?
- a80c734f: I forward web traffic through a router to an internal server, but once I apply an outbound filter on the router interface, external clients' HTTPS requests get no response. Why?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.