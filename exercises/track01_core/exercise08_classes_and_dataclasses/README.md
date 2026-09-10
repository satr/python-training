# Classes and dataclasses

## Theory

A dataclass is a concise model for related attributes. A regular class can
manage a collection and protect its rules through methods. Instance attributes
must be created per object so instances do not accidentally share state.

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
