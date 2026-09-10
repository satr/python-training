# Classes and dataclasses

## Theory

A dataclass is a concise model for related attributes. A regular class can
manage a collection and protect its rules through methods. Instance attributes
must be created per object so instances do not accidentally share state.

## Learn before coding

`@dataclass` generates an initializer for fields, so `Point(2, 3)` can create
an object with `point.x` and `point.y`; a default such as `done: bool = False`
is used when omitted. A container class keeps private state on `self`, for
example `self.items = []`, and methods update that state through
`self.items.append(...)`. Plan each operation as lookup, validation, state
change, and return value. Decide how blank names and repeated names behave,
preserve insertion order with a list, and do not create a new container for
each method call.

## Task

Create the `Task` dataclass and implement `TaskList`. `add` strips surrounding
whitespace, rejects blank or duplicate titles, stores tasks in insertion order,
and returns the new task. `complete` returns whether a matching task was found,
and `pending` returns the titles of incomplete tasks in insertion order.

## Run

```bash
make 01_core_08_classes_and_dataclasses
```

## Further practice

Add task removal and a method that returns completed task titles.
