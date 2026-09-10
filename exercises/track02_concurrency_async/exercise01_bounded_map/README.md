# Bounded map

## Theory

`ThreadPoolExecutor` is useful for blocking I/O. Its `map` operation limits
workers, preserves input order, and re-raises worker exceptions when results
are consumed.

## Task

Implement `bounded_map`. Validate the worker count, evaluate every input
exactly once, preserve result ordering, and propagate task failures.

## Run

```bash
make 02_concurrency_01_bounded_map
```

## Further practice

Implement an unordered variant and compare throughput for uneven tasks.
