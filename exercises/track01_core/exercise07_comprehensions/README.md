# Comprehensions

## Theory

Comprehensions build a new collection by transforming or filtering an
iterable. They are most useful when the expression and condition stay short
enough to read at a glance.

## Learn before coding

A dictionary comprehension looks like
`{key: value * 0.9 for key, value in prices.items()}`; a list comprehension
can filter with `[name for name in names if name.startswith("A")]`.
For unrelated data, `{n: n * n for n in [2, 3]}` maps each input and
`[n for n in [2, 5, 8] if n > 4]` keeps selected values. First write the
equivalent loop, identify the transformed value and the filter, then shorten
it. Create a new result rather than changing the input dictionary, and decide
whether output ordering follows input insertion order.

## Task

Implement `discounted_prices` as a new dictionary whose values are reduced by
the given percentage. Implement `affordable_items` as a sorted list of names
whose prices are less than or equal to `maximum`. Do not mutate the inputs.

## Run

```bash
make 01_core_07_comprehensions
```

## Further practice

Create a nested comprehension that groups affordable items by price range.
