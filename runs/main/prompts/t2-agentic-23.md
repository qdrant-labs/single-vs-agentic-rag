You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- d04bf0e4: Besides provider documentation, what general way works to find out the attributes of any Terraform object you can refer to in an expression?
- 498be774: I want agents' Cisco phones to auto-dial a customer list. What is this feature called, and which Cisco product is the cheaper, simpler option for it?
- d13d5291: I'm designing storage for a chat bot's access rights, where users can have rights per channel and also globally. How should I lay out the tables?
- 7bad4c4c: Is it safe to tell everyone which password hash my site uses if I publish its source code, and what alternative is suggested if the site owner is uneasy about public code?
- 6595dcab: How can I raise PostgreSQL's 32 TB maximum table size, and what limit do I get?
- d07eb5fc: Why do many web API designers still put the release number in the endpoint path despite purists' objections?
- b7e647db: Which ImageMagick option, together with which escape sequence, writes an image's own filename as text in a corner of the image?
- dc97107a: In TCP as defined in RFC 793, what inequality must hold for an incoming ACK to count as an acceptable acknowledgment?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.