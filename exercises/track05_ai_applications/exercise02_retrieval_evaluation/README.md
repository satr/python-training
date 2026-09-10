# Retrieval evaluation

## Theory

Retrieval quality must be measured on a representative labeled dataset.
Precision@k measures result relevance, recall@k measures relevant-item
coverage, and reciprocal rank rewards placing the first relevant result early.

## Task

Implement per-query metrics and macro averages. Handle short rankings,
duplicate retrieved IDs, empty relevant sets, and invalid `k` explicitly.

## Run

```bash
make exercise EXERCISE=exercises/track05_ai_applications/exercise02_retrieval_evaluation
```

## Further practice

Add nDCG and report metrics by query category.
