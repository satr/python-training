# Bounded map

## Theory

`ThreadPoolExecutor` is useful for blocking I/O. Its `map` operation limits
workers, preserves input order, and re-raises worker exceptions when results
are consumed.

## Learn before coding

This executor runs submitted callables with at most two workers:

```python
concurrent.futures.ThreadPoolExecutor(max_workers=2)
```

Its `map` method applies a function and yields results in input order even if
work finishes differently:

```python
executor.map(function, [2, 4, 6])
```
For example, mapping this function produces three corresponding values:

```python
lambda number: number * 10
```

- Manage the executor and inputs carefully:
  - Validate a positive worker count before submitting work.
  - Materialize an iterable only once.
  - Use a context manager so workers shut down.
- Preserve input order rather than sorting by completion time, and allow an
  exception from the callable to reach the caller.

## Task

- Implement `bounded_map` with these guarantees:
  - Validate the worker count.
  - Evaluate every input exactly once.
  - Preserve result ordering.
  - Propagate task failures.

## Run

```bash
make 02_concurrency_01_bounded_map
```

## Further practice

Implement an unordered variant and compare throughput for uneven tasks.
