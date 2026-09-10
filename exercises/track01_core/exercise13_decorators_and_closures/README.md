# Decorators and closures

## Theory

A closure can retain state from the scope where it was created. A decorator
wraps a callable to add behavior while `functools.wraps` keeps the original
callable's metadata available.

## Learn before coding

A decorator receives a function and returns a wrapper:
`def decorate(function):` followed by `def wrapper(value): return function(value)`
and `return wrapper`. A closure keeps variables from the enclosing call, so a
`cache = {}` created when decorating can be reused by later calls. For example,
a square function can cache its integer results.

- A caching wrapper should:
  - Check the cache before calling the wrapped function.
  - Cache successful returns only.
  - Use `functools.wraps(function)` to retain the original metadata.
- Consider repeated arguments and recursive calls separately.

## Task

- Implement `memoize_int` with these wrapper requirements:
  - Cache successful results by integer argument.
  - Do not cache exceptions.
  - Preserve wrapped metadata.
- Use it with `fibonacci`, which raises `ValueError` for negative inputs.

## Run

```bash
make 01_core_13_decorators_and_closures
```

## Further practice

Track cache hits and add a method that clears a decorated function's cache.
