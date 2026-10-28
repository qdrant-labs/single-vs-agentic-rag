You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, run the context command once: it returns the passages a retrieval system found for that question. You cannot search again.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" context <run>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d1a89c98: Why is encapsulating translations in a separate normalized table better than adding a column for each language?
- 00fd739e: I keep contacts for a small church group in one wide table with a column per detail. Should I break out separate tables for things like addresses and churches?
- f28805b9: How much memory would be needed for a WordPress site with 8,000 hits per day with occasional spikes?
- a31c4cc1: Why is it considered a code smell to have a CompanyDao use an EmployeeDao internally?
- f21d09c5: I'm new to building apps for Google's phone OS and the official developer site has no clear reading order. What did one person use to get a guided overview before reading it?
- 59114073: On Ubuntu, which package and command let me percent-encode a local path in a shell script so I can build a link starting with the file scheme?
- 5b5936e9: For an HP P410 RAID with Samsung 830 SSDs on Debian 6.0, which change gives the greatest performance improvement?
- c87f1c47: What kind of encryption would stop a cloud provider from decrypting users' backups for court orders, and what kind of encryption does Google actually apply to WhatsApp chat backups stored on Google Drive?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.