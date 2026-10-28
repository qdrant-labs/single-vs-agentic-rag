You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 2c7b8790: How can a developer deal with accumulating technical debt without asking a non-technical manager for a big-bang rewrite: what goes quietly into every estimate, and where should larger changes be made?
- 0f0478c4: What kind of encryption would stop a cloud provider from decrypting users' backups for court orders, and what kind of encryption does Google actually apply to WhatsApp chat backups stored on Google Drive?
- be75add4: A host answers telnet fine, but an openssl TLS connection to it fails with "No route to host". The name has both A and AAAA records. What is the likely cause?
- 6dbbaea3: Why does Yubico not let users supply their own key material to an authenticator, in terms of what its attestation can promise?
- 3ea292a4: A colleague says that managing our deployments through pull requests in a repository means we've adopted the whole cultural philosophy of joining development and operations. Is that right?
- a6d7ca10: Of the 4,096 possible values in the 12-bit tag field on Ethernet trunks, why can only 4,094 be used, and what are the two excluded values for?
- 9eab912a: How can I raise PostgreSQL's 32 TB maximum table size, and what limit do I get?
- 1d107f9e: How do I let a parameter choose between different multi-column sort orders in a SQL Server ORDER BY, and why does it fail with a conversion error when the sorted columns have different data types?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.