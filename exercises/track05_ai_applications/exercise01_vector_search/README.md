# Vector search

## Theory

Embeddings place items in a vector space. Cosine similarity compares direction
rather than magnitude. Production retrieval must define validation, tie
breaking, and top-k behavior.

## Learn before coding

For vectors `a` and `b`, the dot product is `sum(x * y for x, y in zip(a,
b))`; the Euclidean norm is `sqrt(sum(x * x for x in a))`. Cosine similarity
divides the dot product by both norms, so `[1, 0]` and `[0, 1]` are
orthogonal.

- Validate vector edge cases:
  - Require equal, non-empty lengths.
  - Handle a zero norm deliberately.
- For search:
  - Compute one score per document.
  - Sort by the specified score and tie-break rule.
  - Slice to `limit`, rejecting invalid limits rather than relying on slicing
    quirks.

## Task

- Implement cosine similarity and top-k search without third-party libraries.
- Reject empty, mismatched, and zero vectors.
- Rank ties by document ID.

## Run

```bash
make 05_ai_applications_01_vector_search
```

## Further practice

Normalize vectors at index time and compare dot-product search.
