# Typing and protocols

## Theory

A type variable links input and output types in a generic function. A protocol
describes required behavior instead of requiring inheritance, allowing static
type checkers to recognize structurally compatible objects.

## Learn before coding

`first_matching([3, 8, 11], lambda number: number % 2 == 0)` calls the
predicate on each value and returns the first match, or `None` after the
iteration ends. A `Protocol` describes behavior rather than inheritance:
anything with `describe(self) -> str` can satisfy `Describable`. A reusable
pattern is loop, test, return immediately on success, then return `None`;
for describing, loop and append each method result. Accept iterables without
indexing because they may be generators, and do not call a predicate or
description method more times than necessary.

## Task

Implement generic `first_matching`, returning the first item accepted by its
predicate or `None`. Define `Describable` with a `describe() -> str` method and
implement `describe_all` for any iterable of compatible objects.

## Run

```bash
make 01_core_14_typing_and_protocols
```

## Further practice

Create a protocol for objects that can be saved and a generic filtering helper.
