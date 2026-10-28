# Question generation instructions (given verbatim to generator sub-agents)

Common: Read the packet file. For every item, write one question and a reference answer.
Output one JSON object per line to the output file, nothing else:
{"item": "<item key>", "type": "<type>", "question": "...", "answer": "...", "evidence": [<chunk ids>], "support": "<short quote from the source that states the answer>"}
- The answer must be a specific, checkable fact from the source (a command, option, setting,
  value, cause, or concrete step), at most 25 words (40 for multi).
- The question must make sense to someone who has not seen the thread, and must not mention
  "the thread", "the answer", "the post", or the site.
- Do not write questions answerable from general knowledge alone; the answer should depend on
  the specifics in the source.
- If an item cannot support a good question, output {"item": "<key>", "type": "<type>", "skip": "<reason>"}.

straightforward: the question may use the same terms as the thread title and answer.
semantic: phrase the question the way a user would describe their situation, without reusing
the distinctive terms of the title or answer (no command names, option names, error strings,
or product names from the thread unless there is no other way to ask).
multi: the answer must need one fact from THREAD A and one from THREAD B; neither thread alone
answers it fully. Evidence must include at least one chunk id from each thread.
unanswerable: the source thread will NOT be in the knowledge base. Ask for a specific fact it
states, phrased naturally. Put the fact in "answer" for our records and use "evidence": [].

## Round 2 addition for unanswerable packets (unanswerable_4 and later)
In round 1, most unanswerable questions turned out to be answered by some other thread in the
1M-chunk index. For these packets, ask for the most thread-specific fact the answer states
(an exact version, setting value, error code, flag combination, or product-specific step)
that would be unlikely to appear in other answers. The question must still be something a
practitioner would plausibly ask.
