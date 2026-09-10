# Command-line arguments

## Theory

`argparse` turns command-line strings into typed values. Keep parser creation
separate from program behavior, and accept an explicit `argv` in functions so
tests do not depend on the process command line.

## Task

Build a parser with the positional `name` argument and the optional `--count`
and `--shout` arguments. Render the greeting, keep `main(argv)` testable, and restrict count
to the safe range 1 through 1000.

## Run

```bash
make 01_core_15_command_line_arguments
```

## Further practice

Add an optional `--prefix` argument while keeping the rendering function
independent of `sys.argv`.
