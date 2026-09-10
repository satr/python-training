# Classes and dataclasses

## Theory

A dataclass is a concise model for related attributes. A regular class can
manage a collection and protect its rules through methods. Instance attributes
must be created per object so instances do not accidentally share state.

## Learn before coding

`@dataclass` generates an initializer for fields, so `Point(2, 3)` can create
an object with `point.x` and `point.y`. A field can declare a default:

```python
done: bool = False
```

A container class keeps private state on `self`, for example:

```python
self.items = []
self.items.append(new_item)
```

- Plan each operation in stages:
  - Look up existing state.
  - Validate the request.
  - Change state and return the required value.
- Decide how blank and repeated names behave, preserve insertion order with a
  list, and keep one container across method calls.

## Task

- Create the `Task` dataclass and implement `TaskList`.
- Implement each method's contract:
  - `add` strips whitespace, rejects blank or duplicate titles, stores tasks in
    insertion order, and returns the new task.
  - `complete` returns whether a matching task was found.
  - `pending` returns incomplete titles in insertion order.

## Run

```bash
make 01_core_08_classes_and_dataclasses
```

## Further practice

Add task removal and a method that returns completed task titles.
