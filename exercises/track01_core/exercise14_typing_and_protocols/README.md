# Typing and protocols

## Theory

A type variable links input and output types in a generic function. A protocol
describes required behavior instead of requiring inheritance, allowing static
type checkers to recognize structurally compatible objects.

## Learn before coding

`first_matching([3, 8, 11], lambda number: number % 2 == 0)` calls the
predicate on each value and returns the first match, or `None` after the
iteration ends. A `Protocol` describes behavior rather than inheritance:
anything with `describe(self) -> str` can satisfy `Describable`.

- To find a match:
  - Loop and test each value.
  - Return immediately on success.
  - Return `None` only after the iteration ends.
- To describe objects, loop and append each method result.
- Accept iterables without indexing because they may be generators, and avoid
  unnecessary predicate or description calls.

## Task

- Implement generic `first_matching`, returning the first item accepted by its
  predicate or `None`.
- Define and use the description protocol:
  - `Describable` has a `describe() -> str` method.
  - `describe_all` accepts any iterable of compatible objects.

## Run

```bash
make 01_core_14_typing_and_protocols
```

## Further practice

Create a protocol for objects that can be saved and a generic filtering helper.
