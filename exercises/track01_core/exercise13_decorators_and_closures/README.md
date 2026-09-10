# Decorators and closures

## Theory

A closure can retain state from the scope where it was created. A decorator
wraps a callable to add behavior while `functools.wraps` keeps the original
callable's metadata available.

## Task

Implement `memoize_int` to cache successful results by integer argument,
without caching exceptions, and preserve wrapped metadata. Use it with
`fibonacci`, which raises `ValueError` for negative inputs.

## Run

```bash
make 01_core_13_decorators_and_closures
```

## Further practice

Track cache hits and add a method that clears a decorated function's cache.
