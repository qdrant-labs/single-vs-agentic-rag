# Single-Pass vs Agentic RAG on Qdrant

The benchmark behind the Qdrant article "Every RAG Obituary Was Half Right". It compares one search per question with an agent that can search and read more, using the same data, model and questions for both.

## Setup

- **Data:** 1,000,000 chunks of Stack Exchange answers from seven technical sites (Server Fault, Unix & Linux, Software Engineering, DBA, Security, Network Engineering, DevOps).
- **Index:** Qdrant Cloud with `sentence-transformers/all-MiniLM-L6-v2` embeddings through Cloud Inference, and int8 scalar quantization with rescoring.
- **Model:** Claude Sonnet 5.5 for both pipelines.
- **Single pass:** one dense search on the question, top 10 results, one answer.
- **Agent:** search (10 results a page) and open a full answer, up to 6 calls in total.
- **Answer rule (both):** answer only from retrieved text and cite chunk ids, or say "not found".
- **Questions:** 200, 50 per type:
  - straightforward;
  - reworded (semantic);
  - multi-document (two threads);
  - unanswerable.

  They were written from the corpus and checked by independent verifiers. Unanswerable questions were confirmed absent with dense and BM25 searches.
- **Runs:** 3 trials per pipeline, 1,200 runs in total.
- **Grading:** blind LLM judges graded every run against the reference answer. A second judge re-graded a 20% sample and agreed on 99.6% of labels.

## Results

| Question type | Single pass correct | Agent correct | Agent search/open calls per question |
|---|---|---|---|
| Straightforward | 98.0% | 96.7% | 1.12 |
| Reworded | 47.3% | 92.0% | 1.69 |
| Multi-document | 22.7% | 69.3% | 3.15 |
| Unanswerable (said "not found") | 100.0% | 98.0% | 5.93 |

- On answerable questions, the agent scored 86% against 56% for the single pass.
- `REPORT.md` has the full results: unsupported answers, refusals, tokens, latency p50/p95, paired tests, judge agreement and limitations. Section 10 covers a follow-up test of a weak-retrieval gate.

## What's Here

| Path | Contents |
|---|---|
| `DESIGN.md` | The design, fixed before the runs |
| `REPORT.md` | Results and limitations |
| `scripts/` | Every step, from corpus build to analysis |
| `data/questions.json` | The frozen 200 questions with reference answers and evidence chunk ids (sha256 in `questions.sha256`) |
| `data/qgen/`, `data/verify/` | Question generation and verification packets, instructions and outputs |
| `data/judge/` | Judge packets, instructions and labels |
| `runs/main/results.jsonl` | One row per run: answer, cited chunks, calls, queries, chunks shown, Qdrant time |
| `runs/main/events.jsonl` | Every tool call the runs made |
| `runs/main/prompts/` | The exact prompts given to the run sub-agents |
| `runs/main/report.md`, `summary.json`, `latency.json`, `gate_*` | Analysis outputs |

The raw dumps, the 1M-chunk file and the BM25 index are not included. The scripts rebuild them.

## Reproduce

1. **Download the dumps.** Get the seven site archives listed in `data/raw/SHA256SUMS` from [archive.org/details/stackexchange](https://archive.org/details/stackexchange) into `data/raw/`.
2. **Build the corpus:**
   ```
   python -I scripts/build_corpus.py extract
   python -I scripts/build_corpus.py parse
   python -I scripts/build_corpus.py chunk
   python -I scripts/select_sources.py
   python -I scripts/kw_index.py build
   ```
3. **Upload to Qdrant.** Set `QDRANT_URL` and `QDRANT_API_KEY`, then run:
   ```
   python -I scripts/upload.py create
   python -I scripts/upload.py upload
   python -I scripts/upload.py index
   ```
4. **Start the runs.** Run `python -I scripts/make_runs.py`, then start the tool server with `python -I scripts/bench_server.py main`.
   - The runs were driven by Claude Code sub-agents, 8 questions each, one per prompt file in `runs/main/prompts/`.
   - They call the tool server through `scripts/bench_tool.py`.
5. **Grade and analyze:**
   - Run `python -I scripts/make_judge.py`, grade the packets in `data/judge/` with `data/judge/INSTRUCTIONS.md`, then run `python -I scripts/latency.py` and `python -I scripts/analyze.py`.
   - `latency.py` reads Claude Code transcripts, so on a rerun latency comes from wherever your model calls are logged.

## Limitations

- **Accuracy figures are exact; cost figures are estimates.** Accuracy, refusals and call counts come straight from the logs. Model tokens and latency were rebuilt from Claude Code transcripts, because each sub-agent worked on several questions at once.
- **Narrow setup:** one corpus, one model and a small dense-only embedder. A stronger first-stage search could narrow the gap on reworded questions.
- **LLM-written and LLM-graded:** the questions were written by LLMs from specific chunks, and graded by LLM judges.
- **Run notes:** see `runs/main/NOTES.md`. It records one run that saved the answer "NOT_FINAL" by accident.

## Data License

The corpus, questions and packets are derived from the [Stack Exchange data dump](https://archive.org/details/stackexchange), licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Content belongs to its Stack Exchange authors.
