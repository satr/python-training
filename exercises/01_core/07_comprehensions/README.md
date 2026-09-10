# Comprehensions

## Theory

Comprehensions build a new collection by transforming or filtering an
iterable. They are most useful when the expression and condition stay short
enough to read at a glance.

## Learn before coding

A dictionary comprehension can transform every value:

```python
{key: value * 0.9 for key, value in prices.items()}
```

A list comprehension can filter:

```python
[name for name in names if name.startswith("A")]
```

For unrelated data, these examples map each input and keep selected values:

```python
{n: n * n for n in [2, 3]}
[n for n in [2, 5, 8] if n > 4]
```

First write the equivalent loop, then identify the transformed value and filter
before shortening it.

- Preserve collection behavior:
  - Create a new result rather than changing the input dictionary.
  - Decide whether output ordering follows input insertion order.

## Task

- Implement both collection transformations without mutating the inputs:
  - `discounted_prices` returns a new dictionary with values reduced by the
    given percentage.
  - `affordable_items` returns a sorted list of names whose prices are less
    than or equal to `maximum`.

## Run

```bash
make 01_core_07_comprehensions
```

## Further practice

Create a nested comprehension that groups affordable items by price range.
