# Files and context managers

## Theory

Text files must be opened with an explicit encoding when their format requires
one. A `with` statement closes the file even if processing fails. Opening a
file in write mode replaces its previous contents.

## Learn before coding

Use a context manager so the file closes even when reading fails:

```python
with path.open("r", encoding="utf-8") as file:
    text = file.read()
```

Writing uses `"w"` and `file.write(text)`. `line.strip()` removes surrounding
whitespace, while `line.startswith("#")` identifies a comment.

- For loading, follow a clear sequence:
  - Open, iterate, and normalize each line.
  - Skip intentionally empty records.
  - Return the collected values.
- For saving, write each record plus `"\n"` and count records successfully
  consumed.
- Choose text mode and UTF-8 explicitly; remember that `"w"` replaces a file.

## Task

- Implement `load_tasks` and `save_tasks` using UTF-8.
- When loading:
  - Strip surrounding whitespace.
  - Ignore blank lines and lines whose first non-space character is `#`.
- When saving:
  - Overwrite the file with one task per line.
  - Return the number of tasks consumed from the iterable.

## Run

```bash
make 01_core_11_files_and_context_managers
```

## Further practice

Support an append mode and report malformed task lines with their line number.
