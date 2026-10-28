You answer questions about Linux, servers, databases, networking, security and software engineering using a knowledge base of community answers. For each question below, search the knowledge base: you may search several times with different wording, look at the next page of results, and open a post to read the whole answer. Each question allows at most 6 search/open calls.

Answer only from text the tool returned. Record a short answer (one or two sentences) together with the ids of the chunks that support it. If the retrieved text does not contain the answer, record not_found instead. Do not answer from your own knowledge.

Commands (Bash):
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" search <run> "<query>" [page]
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" open <run> <post number>
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" answer <run> <chunk ids, comma-separated> "<answer>"
python -I "C:/Users/Home Laptop/rag-bench/scripts/bench_tool.py" not_found <run>

Rules: use only these commands. Apart from this file, do not read, list, grep or search any files or folders, and do not use any other tool. Record exactly one answer per question, then move on.

Questions (run id: question):
- 2800490e: My PHP web service parses XML sent by browsers, and I'm worried the parser could be tricked into reading local files or probing internal hosts. Which PHP call mitigates this?
- 03c38d41: Why do many web API designers still put the release number in the endpoint path despite purists' objections?
- 921bdef6: After upgrading my Linux desktop environment, opening a link from another app no longer switches me to the workspace where my browser window lives. Which window behavior setting restores that?
- d951d055: With Apache's mod_bw, how can I limit files over 1MB to 200kb/s?
- d12ee66f: For an HP P410 RAID with Samsung 830 SSDs on Debian 6.0, which change gives the greatest performance improvement?
- 42585460: To script a login to criticker.com with curl and then fetch protected pages, which URL should the credentials be posted to?
- 337a7efa: What is the difference between nscd and sssd, and should both run at the same time?
- 80748c08: What must a VoIP customer and provider maintain so that E911 emergency calls carry more than just a street address?

When every question has an answer recorded, reply with one line: how many you answered and how many you marked not_found.