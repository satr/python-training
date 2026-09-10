# Lists and tuples

## Theory

Lists are mutable collections that preserve order. Tuples are useful for a
fixed group of results. Built-ins such as `min`, `max`, `sum`, and `sorted`
express common collection operations clearly.

## Task

Implement `summarize_scores` to return the minimum, maximum, and average, or
`None` for no scores. Implement `top_scores` to return up to `limit` values in
descending order without changing the input. A non-positive limit returns an
empty list.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise05_lists_and_tuples
```

## Further practice

Return the median and remove duplicate values from the ranking.
