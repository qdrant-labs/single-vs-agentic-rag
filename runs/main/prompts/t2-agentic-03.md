You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- cbdac5b2: Of the 4,096 possible values in the 12-bit tag field on Ethernet trunks, why can only 4,094 be used, and what are the two excluded values for?
- d7f655e8: What kind of encryption would stop a cloud provider from decrypting users' backups for court orders, and what kind of encryption does Google actually apply to WhatsApp chat backups stored on Google Drive?
- 3f300706: How can I build a Git commit history from successive snapshots of a code base, setting the author name and date on each imported commit?
- a1cfc61f: Should a command's --help usage message go to stderr or stdout, and where should the usage message for an invalid option go?
- f6ea827e: Why is encapsulating translations in a separate normalized table better than adding a column for each language?
- 0fbcf911: How can I check the free memory of a Jenkins build executor?
- e2a75f27: Why is it considered a code smell to have a CompanyDao use an EmployeeDao internally?
- 3f51e7f8: Apache writes its files into a private, hash-named directory under /tmp. What setting causes that, and how can I change it for Apache's unit without editing the package-supplied unit file?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.