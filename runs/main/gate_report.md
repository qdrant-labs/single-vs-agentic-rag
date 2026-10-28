# Gated pipeline: one search, escalate to the agent when retrieval looks weak

## 1. Signal separation (AUC; 0.5 = chance; weak = window lacks the evidence)

| signal | all 200 | answerable 150 | straightforward | semantic | multi |
|---|---|---|---|---|---|
| max_score | 0.79 | 0.77 | 0.82 | 0.55 | 0.60 |
| dense_variance | 0.82 | 0.84 | 0.94 | 0.72 | 0.60 |
| dense_sparse_overlap | 0.73 | 0.73 | 0.73 | 0.57 | 0.67 |

Weak share by type: straightforward 6%, semantic 68%, multi 86%, unanswerable 100%

## 2. Held-out results (500 random 50/50 splits; floor = Youden point on the calibration half)

| pipeline | escalated | answerable correct | unanswerable refused | calls / q | retrieved tokens / q | latency p50 / p95 s |
|---|---|---|---|---|---|---|
| single pass | 0% | 56.1% | 100.0% | 1.00 | 997 | 3.1 / 6.8 |
| always agent | 100% | 86.1% | 97.9% | 2.96 | 2727 | 4.9 / 20.3 |
| max_score | 57% | 76.8% | 97.9% | 3.04 | 2323 | 4.2 / 19.3 |
| dense_variance | 68% | 82.7% | 97.9% | 3.32 | 2443 | 4.6 / 20.2 |
| dense_sparse_overlap | 69% | 81.1% | 98.5% | 3.28 | 2390 | 4.4 / 20.2 |
| chosen on calibration | 66% | 81.3% | 97.9% | 3.26 | 2419 | 4.5 / 20.0 |
| random, same escalation rate | 66% | 75.7% | 98.6% | 2.97 | 2148 | 3.9 / 18.9 |
| oracle (escalate answerable misses only) | 40% | 88.6% | 100.0% | 2.05 | 1541 | 3.4 / 15.4 |

## 3. By question type (dense_variance < 0.001839, floor fitted on all 200: descriptive, not held out)

| type | escalated | single correct | gated correct | agent correct | calls / q gated vs agent | latency p50 s gated vs agent |
|---|---|---|---|---|---|---|
| straightforward | 24% | 98.0% | 97.3% | 96.7% | 1.36 vs 1.12 | 3.0 vs 2.8 |
| semantic | 88% | 47.3% | 90.7% | 92.0% | 2.54 vs 1.69 | 3.4 vs 3.4 |
| multi | 92% | 22.7% | 66.0% | 69.3% | 3.93 vs 3.15 | 6.4 vs 6.4 |
| unanswerable | 88% | 100.0% | 98.0% | 98.0% | 6.21 vs 5.93 | 15.2 vs 15.2 |

## 4. Trade-off curve: escalate the weakest x% by dense_variance (all 200, in-sample)

| escalated | answerable correct | unanswerable refused | calls / q | retrieved tokens / q | latency p50 / p95 s |
|---|---|---|---|---|---|
| 0% | 56.0% | 100.0% | 1.00 | 997 | 3.1 / 6.9 |
| 10% | 59.8% | 99.3% | 1.39 | 1258 | 3.2 / 11.4 |
| 20% | 65.1% | 99.3% | 1.75 | 1502 | 3.3 / 16.2 |
| 30% | 70.7% | 99.3% | 2.06 | 1691 | 3.3 / 17.2 |
| 40% | 74.2% | 99.3% | 2.33 | 1841 | 3.4 / 18.4 |
| 50% | 79.1% | 98.0% | 2.70 | 2059 | 3.8 / 18.7 |
| 60% | 79.8% | 98.0% | 3.07 | 2315 | 4.4 / 19.5 |
| 70% | 83.3% | 98.0% | 3.42 | 2513 | 4.8 / 20.8 |
| 80% | 85.1% | 98.0% | 3.68 | 2665 | 5.0 / 20.8 |
| 90% | 85.6% | 98.0% | 3.84 | 2712 | 5.0 / 20.8 |
| 100% | 86.0% | 98.0% | 3.97 | 2737 | 5.0 / 20.8 |

## 5. Side estimate: always agent with a smaller search budget (from the logs, conservative)

| budget | answerable correct | unanswerable refused | calls / q | latency p50 / p95 s |
|---|---|---|---|---|
| 2 | 72.2% | 100.0% | 1.57 | 4.3 / 7.3 |
| 3 | 80.4% | 100.0% | 1.99 | 4.9 / 10.5 |
| 4 | 82.4% | 100.0% | 2.34 | 4.9 / 13.8 |
| 6 | 86.0% | 98.0% | 2.97 | 4.9 / 20.5 |