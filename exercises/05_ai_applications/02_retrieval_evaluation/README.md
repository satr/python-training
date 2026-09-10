# Retrieval evaluation

## Theory

Retrieval quality must be measured on a representative labeled dataset.
Precision@k measures result relevance, recall@k measures relevant-item
coverage, and reciprocal rank rewards placing the first relevant result early.

## Learn before coding

For ranked IDs, precision at `k` is relevant hits in the first `k` results
divided by the number examined, while recall divides hits by all relevant
IDs. Reciprocal rank uses this formula for the first relevant result:

```python
1 / position
```

It is zero if no relevant result appears.
For example, retrieved `("b", "a")`, relevant `{"a"}`, and `k=2` has one hit
and first relevant position two.

- Evaluate each case in a consistent order:
  - Validate `k` before indexing.
  - Clamp the ranking to `k`.
  - Apply the contract's rule for duplicate IDs.
  - Handle an empty relevant set consistently.
  - Average each metric across cases.

## Task

Implement per-query metrics and macro averages. Handle short rankings,
duplicate retrieved IDs, empty relevant sets, and invalid `k` explicitly.

## Run

```bash
make 05_ai_applications_02_retrieval_evaluation
```

## Further practice

Add nDCG and report metrics by query category.
