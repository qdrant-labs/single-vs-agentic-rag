# Single-pass RAG vs agentic RAG on Qdrant: benchmark design (draft, 2026-10-28)

Goal: find where iterative retrieval measurably helps and where its extra complexity
costs accuracy, tokens, or time. Not to show that either approach wins.

## 1. Infrastructure (decided)
- Qdrant Cloud cluster, v1.19.1, 1 vCPU, ~1.8 GB RAM, ~7.8 GB disk, us-west-1 (AWS).
  The existing collection `scale500k_b1_raw` is left untouched.
- Embeddings: Cloud Inference, `sentence-transformers/all-MiniLM-L6-v2` (384-d, cosine).
  mxbai (1024-d) does not fit this cluster at 1M points.
- Collection `rag_bench_se_1m`: HNSW m=16, ef_construct=100; original vectors on disk,
  int8 scalar quantization kept in RAM with rescoring; payload on disk; payload
  indexes on `site` and `thread_id`.
- LLM: Claude Code sub-agents, one model for both pipelines (see open decision C).
  Accuracy, refusals and call counts are exact. LLM latency and tokens include Claude
  Code's own overhead and are reported as approximate; Qdrant search latency is exact.

## 2. Corpus (~1M points)
- Source: Stack Exchange public data dump (CC BY-SA 4.0), archive.org item
  `stackexchange`. Technical sites only (see open decision A).
- Unit: one accepted or positively scored answer, prefixed with its question title,
  split into chunks of at most ~500 characters (MiniLM's 128 to 256-token window).
  Payload: text, site, thread id, post id, score, accepted flag, chunk index.
- Deterministic build: fixed site list, fixed filters, fixed seed, SHA-256 of every
  downloaded archive recorded in `data/manifest.json`.
- Held-out set: threads used for unanswerable questions, plus every thread linked to
  them as a duplicate or related post, are excluded from the index before upload.

## 3. Questions (~200, four types of ~50)
| Type | What it tests | Ground truth |
|---|---|---|
| Straightforward | answer stated in one chunk, question close to its wording | 1 evidence chunk |
| Semantic | same kind of fact, question paraphrased with no shared key terms | 1 evidence chunk |
| Multi-document | needs facts from 2 different threads (from Stack Exchange post links) | 2+ evidence chunks, each required |
| Unanswerable | specific fact that lives only in held-out threads | no evidence in the index |

Construction and verification:
1. A generator sub-agent drafts each question from sampled threads, with a short
   reference answer and evidence chunk ids.
2. An independent verifier (fresh context, different model from the generator) checks
   every item: the evidence supports the answer, the question is unambiguous, multi-doc
   items cannot be answered from one chunk, and the answer is not given away verbatim.
3. Unanswerable items: the verifier runs dense and keyword (BM25) searches over the
   full index (top 50 each) and confirms no chunk answers the question.
4. Items that fail are fixed or dropped. Final set frozen with a hash before any run.

## 4. Pipelines (same data, model, questions, and answer rule)
- Single-pass RAG: one dense search with the question text, top 10 chunks shown, one
  answer. Retrieval runs in the harness, not chosen by the model.
- Agentic RAG: `search(query, page)` (10 per page) and `open(thread)` to read a whole
  answer, up to 6 search/open calls (fixed budget), then answer.
- Shared rule: answer only from retrieved text, cite chunk ids, or reply NOT_FOUND if
  the retrieved text does not contain the answer.
- Both pipelines call the same tool server, which times every Qdrant call and logs
  every event with timestamps.

## 5. Trials and blinding
- 3 trials per pipeline (2 pipelines x 200 questions x 3 = 1,200 runs).
- Small batches (about 8 questions per sub-agent), questions of all types mixed, no two
  related questions in one batch, opaque run ids, conditions hidden from the model.

## 6. Grading (fixed before any run)
- A judge sub-agent, blind to pipeline and trial, labels each answer against the
  reference answer and evidence: correct, incorrect, or NOT_FOUND.
- Answerable question: correct; incorrect = unsupported answer; NOT_FOUND = missed.
- Unanswerable question: NOT_FOUND = correct refusal; any answer = unsupported answer.
- Judge check: a second judge on a 20% sample; agreement reported.

## 7. Metrics and report
Per pipeline and question type, mean and range over trials:
- answer accuracy, unsupported-answer rate, correct-refusal rate
- retrieval calls per question
- tokens per question (approximate)
- latency: Qdrant search p50/p95 (exact); end-to-end p50/p95 from first tool call to
  final answer (includes LLM time, approximate)
- paired comparison per question (McNemar), and where each pipeline wins or loses.

## 8. Reproducibility
- Everything in `rag-bench/`: download, build, upload, question generation and
  verification, runs, grading, analysis. Each step writes its outputs with a hash.
- Credentials only from `QDRANT_URL` and `QDRANT_API_KEY` in the environment.

## Decisions (2026-10-28)
A. Data: 7 sites, ~2.6 GB: serverfault, unix, softwareengineering, dba, security,
   networkengineering, devops. Checksums in data/raw/SHA256SUMS.
B. Embeddings: Cloud Inference for all ~1M chunks (~130M tokens), approved.
C. LLM: Claude Sonnet 5.5 (Claude Code sub-agents) for both pipelines.
Probe results: Cloud Inference upsert ~700 docs/s (256-doc batch); query round trip from
this laptop ~116 ms median.
