# Judge instructions (given verbatim to judge sub-agents)

Each item is one system's response to a question about a technical knowledge base. You do
not know which system produced it. For every item, output one JSON object per line:
{"jid": "<judge item id>", "label": "correct" | "partial" | "incorrect" | "not_found",
 "cited_support": "yes" | "no" | "n/a", "reason": "<one short sentence>"}

label:
- not_found: the system answered NOT_FOUND.
- correct: the answer states the reference answer's key fact(s), possibly in other words or
  with harmless extra detail. For multi-part references, every part must be present.
- partial: some but not all required facts, or the right fact mixed with a wrong one.
- incorrect: the answer is wrong, does not answer the question, or the question has no
  answer in the knowledge base and the system answered anyway.

cited_support: "yes" if the chunks the system cited actually state what the system
answered, "no" if they do not, "n/a" for NOT_FOUND.

Judge only against the reference and the cited text, not your own knowledge.
