You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 9abec871: I applied IP-based packet filter rules to a switch port carrying several tagged VLANs and nothing is filtered. Why is that, and where do the rules belong?
- 87b82fbf: On a pair of Cisco Nexus switches sharing a multi-chassis port channel, must the trunk's allowed list of Layer 2 segments match on both switches to avoid the channel being suspended?
- 71398101: Of the 4,096 possible values in the 12-bit tag field on Ethernet trunks, why can only 4,094 be used, and what are the two excluded values for?
- d98ec105: I'm considering enabling Google's experimental faster web transport protocol on my TLS site. Which known attack on compressed headers and cookies is the security concern?
- b65e3695: Why does Python allow 1 + 1.0 but not 1 + "1" when it avoids implicit conversions?
- 141be459: How can I build a Git commit history from successive snapshots of a code base, setting the author name and date on each imported commit?
- e3bab55e: In SSRS, the page setup print options don't change my report's orientation. What do I set in BIDS instead?
- 111e7301: A computer booting with no IP configured asks the network for an address. How can the server reply directly to it rather than shouting to everyone?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.