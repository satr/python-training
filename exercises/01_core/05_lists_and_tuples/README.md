# Lists and tuples

## Theory

Lists are mutable collections that preserve order. Tuples are useful for a
fixed group of results. Built-ins such as `min`, `max`, `sum`, and `sorted`
express common collection operations clearly.

## Learn before coding

Index a list with `items[0]`. A loop visits each item:

```python
for item in items:
    process(item)
```

Use this call when a new ordered list is needed:

```python
sorted(items, reverse=True)
```

`sorted` does not mutate its input. `min`, `max`, and `sum` help summarize
non-empty numbers, while `items[:limit]` safely takes at most a requested
number. For example, this expression gives the two largest values:

```python
sorted([4, 1, 3], reverse=True)[:2]
```

- Before summarizing:
  - Decide what an empty input returns before calling `min` or `max`.
  - Remember that `(lowest, highest, average)` is an ordered, immutable tuple.

## Task

- Implement `summarize_scores` to return the minimum, maximum, and average, or
  `None` for no scores.
- Implement `top_scores` with these rules:
  - Return up to `limit` values in descending order without changing the input.
  - Return an empty list for a non-positive limit.

## Run

```bash
make 01_core_05_lists_and_tuples
```

## Further practice

Return the median and remove duplicate values from the ranking.
