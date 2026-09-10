# Lists and tuples

## Theory

Lists are mutable collections that preserve order. Tuples are useful for a
fixed group of results. Built-ins such as `min`, `max`, `sum`, and `sorted`
express common collection operations clearly.

## Learn before coding

Index a list with `items[0]`, loop with `for item in items`, and use
`sorted(items, reverse=True)` when a new ordered list is needed; `sorted`
does not mutate its input. `min`, `max`, and `sum` help summarize non-empty
numbers, while `items[:limit]` safely takes at most a requested number.
For example, `sorted([4, 1, 3], reverse=True)[:2]` gives the two largest
values. Decide what an empty input returns before calling `min` or `max`, and
remember that a tuple such as `(lowest, highest, average)` is ordered and
immutable.

## Task

Implement `summarize_scores` to return the minimum, maximum, and average, or
`None` for no scores. Implement `top_scores` to return up to `limit` values in
descending order without changing the input. A non-positive limit returns an
empty list.

## Run

```bash
make 01_core_05_lists_and_tuples
```

## Further practice

Return the median and remove duplicate values from the ranking.
