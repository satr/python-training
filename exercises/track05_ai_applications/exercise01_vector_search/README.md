# Vector search

## Theory

Embeddings place items in a vector space. Cosine similarity compares direction
rather than magnitude. Production retrieval must define validation, tie
breaking, and top-k behavior.

## Task

Implement cosine similarity and top-k search without third-party libraries.
Reject empty, mismatched, and zero vectors; rank ties by document ID.

## Run

```bash
make 05_ai_applications_01_vector_search
```

## Further practice

Normalize vectors at index time and compare dot-product search.
