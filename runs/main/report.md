# Single-pass vs agentic RAG on Qdrant: results

200 questions x 2 pipelines x 3 trials = 1200 runs; judge labels 1200, second-judge labels 240.

## 1. Outcomes by question type (mean of 3 trials, per-trial range in brackets)

| type | pipeline | correct | unsupported (partial / incorrect) | missed (NOT_FOUND) |
|---|---|---|---|---|
| straightforward | single | 98.0% [98-98] | 2.0% [2-2] (3 / 0) | 0.0% [0-0] |
| straightforward | agentic | 96.7% [96-98] | 3.3% [2-4] (5 / 0) | 0.0% [0-0] |
| semantic | single | 47.3% [46-48] | 13.3% [12-14] (12 / 8) | 39.3% [38-42] |
| semantic | agentic | 92.0% [90-94] | 6.0% [6-6] (6 / 3) | 2.0% [0-4] |
| multi | single | 22.7% [22-24] | 29.3% [26-34] (44 / 0) | 48.0% [44-52] |
| multi | agentic | 69.3% [68-72] | 23.3% [20-26] (34 / 1) | 7.3% [4-12] |
| unanswerable | single | correct refusal 100.0% [100-100] | answered anyway 0.0% [0-0] | - |
| unanswerable | agentic | correct refusal 98.0% [96-100] | answered anyway 2.0% [0-4] | - |
| all answerable | single | 56.0% | 14.9% | 29.1% |
| all answerable | agentic | 86.0% | 10.9% | 3.1% |

## 2. Paired comparison per question (trial-majority outcome, exact McNemar)

| type | single right | agentic right | only single | only agentic | p |
|---|---|---|---|---|---|
| straightforward | 49/50 | 49/50 | 0 | 0 | 1 |
| semantic | 24/50 | 47/50 | 0 | 23 | 2.4e-07 |
| multi | 11/50 | 37/50 | 2 | 28 | 8.7e-07 |
| unanswerable | 50/50 | 50/50 | 0 | 0 | 1 |
| answerable | 84/150 | 133/150 | 2 | 51 | 3.2e-13 |

## 3. Retrieval: did the run see the reference evidence?

Share of runs whose retrieved text included all / some / none of the reference evidence chunks (the chunks the question was written from; another chunk can also hold the answer).

| type | pipeline | all | some | none | correct when all shown | correct when none shown |
|---|---|---|---|---|---|---|
| straightforward | single | 94% | 4% | 2% | 141/141 | 0/3 |
| straightforward | agentic | 93% | 5% | 2% | 137/139 | 0/3 |
| semantic | single | 32% | 12% | 56% | 48/48 | 12/84 |
| semantic | agentic | 77% | 9% | 13% | 115/116 | 11/20 |
| multi | single | 14% | 54% | 32% | 21/21 | 3/48 |
| multi | agentic | 38% | 50% | 12% | 53/57 | 6/18 |

Where iterative retrieval changed the outcome (answerable questions, per run pair: same question, same trial):

- single-pass top 10 held the evidence (315 run pairs): single correct 237, agentic correct 281; agentic fixed 56, agentic lost 12
- single-pass top 10 missed the evidence (135 run pairs): single correct 15, agentic correct 106; agentic fixed 91, agentic lost 0

## 4. Cost: retrieval calls, tokens, latency

| | single | agentic |
|---|---|---|
| retrieval calls per question (mean) | 1 | 2.97 |
| retrieval calls per question (p95) | 1 | 6 |
| searches / opens per question (mean) | 1.0 / 0.0 | 2.6 / 0.4 |
| runs closed by the 6-call budget | 0 | 10 |
| sequential model rounds per question (mean / p95) | 2.0 / 2.0 | 4.0 / 7.0 |
| retrieved context tokens per question (mean / p95) | 996.8 / 1147.0 | 2736.9 / 6119.5 |
| sub-agent tokens per question, in / out (batched, inflated) | 62435.2 / 462.2 | 146683.8 / 1038.3 |
| Qdrant ms per query (p50 / p95) | 71.3 / 173.4 | 87.9 / 171.5 |
| Qdrant ms per question (p50 / p95) | 71.3 / 173.4 | 187.4 / 666.7 |
| latency s, model + Qdrant, shared-turn split (p50 / p95) | 3.1 / 6.9 | 4.9 / 20.5 |
| latency s, model + Qdrant, full-turn charge (p50 / p95) | 14.5 / 39.6 | 18.7 / 75.7 |
| wall clock s incl. Claude Code tool overhead (p50 / p95) | 16.4 / 52.4 | 28.7 / 96.2 |

Agentic cost by question type (mean calls; latency p50 / p95, model + Qdrant, split):

- straightforward: 1.12 calls; latency agentic 2.8 / 5.2 s vs single 2.9 / 5.1 s; agentic retrieved tokens 1056
- semantic: 1.69 calls; latency agentic 3.4 / 9.9 s vs single 3.0 / 6.9 s; agentic retrieved tokens 1620
- multi: 3.15 calls; latency agentic 6.4 / 23.9 s vs single 3.5 / 7.2 s; agentic retrieved tokens 2788
- unanswerable: 5.93 calls; latency agentic 15.2 / 24.2 s vs single 2.9 / 6.1 s; agentic retrieved tokens 5483

## 5. Measurement checks

- Second judge on 240 runs (20% sample): exact label agreement 99.6%, Cohen's kappa 0.99; on answered items only 99.3% (kappa 0.98); correct-vs-not agreement 99.6%.
  Disagreements: {'correct->partial': 1}
- Same outcome in all 3 trials: single 91% of questions, agentic 84%.
- Cited chunks do not support the answer (judge cited_support = no): single 6/319, agentic 12/439 answers.

## 6. Sensitivity

- without the accidental 'NOT_FINAL' run, single: correct 56.0%, unsupported 14.9%
- without the accidental 'NOT_FINAL' run, agentic: correct 86.2%, unsupported 10.7%
- partial counted as half credit, single: 62.6%
- partial counted as half credit, agentic: 91.0%
- second-judge sample, single (88 answerable runs): correct 47 by judge 1, 46 by judge 2
- second-judge sample, agentic (83 answerable runs): correct 72 by judge 1, 72 by judge 2

Batches with token counts: 150/150; batches matched by more than one transcript: []