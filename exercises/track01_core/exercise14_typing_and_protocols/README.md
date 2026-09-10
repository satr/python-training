# Typing and protocols

## Theory

A type variable links input and output types in a generic function. A protocol
describes required behavior instead of requiring inheritance, allowing static
type checkers to recognize structurally compatible objects.

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
