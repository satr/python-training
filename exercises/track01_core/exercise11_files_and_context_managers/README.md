# Files and context managers

## Theory

Text files must be opened with an explicit encoding when their format requires
one. A `with` statement closes the file even if processing fails. Opening a
file in write mode replaces its previous contents.

## Task

Implement `load_tasks` and `save_tasks` using UTF-8. Loading strips surrounding
whitespace and ignores blank lines and lines whose first non-space character is
`#`. Saving overwrites the file with one task per line and returns the number
of tasks consumed from the iterable.

## Run

```bash
make exercise EXERCISE=exercises/track01_core/exercise11_files_and_context_managers
```

## Further practice

Support an append mode and report malformed task lines with their line number.
