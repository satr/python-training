# Files and context managers

## Theory

Text files must be opened with an explicit encoding when their format requires
one. A `with` statement closes the file even if processing fails. Opening a
file in write mode replaces its previous contents.

## Learn before coding

Use `with path.open("r", encoding="utf-8") as file:` so the file closes even
when reading fails; writing uses `"w"` and `file.write(text)`. `line.strip()`
removes surrounding whitespace, while `line.startswith("#")` identifies a
comment. A reusable sequence is open, iterate, normalize, skip intentionally
empty records, then return the collected values; for saving, write one record
plus `"\n"` and count successful records. Choose text mode and UTF-8
explicitly, avoid treating a blank line as data, and remember that `"w"`
replaces an existing file.

## Task

Implement `load_tasks` and `save_tasks` using UTF-8. Loading strips surrounding
whitespace and ignores blank lines and lines whose first non-space character is
`#`. Saving overwrites the file with one task per line and returns the number
of tasks consumed from the iterable.

## Run

```bash
make 01_core_11_files_and_context_managers
```

## Further practice

Support an append mode and report malformed task lines with their line number.
