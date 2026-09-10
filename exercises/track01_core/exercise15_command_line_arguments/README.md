# Command-line arguments

## Theory

`argparse` turns command-line strings into typed values. Keep parser creation
separate from program behavior, and accept an explicit `argv` in functions so
tests do not depend on the process command line.

## Learn before coding

`argparse.ArgumentParser` defines a command-line interface:
`parser.add_argument("--name", default="reader")` supplies a default, while
`type=int` converts text such as `"3"` to an integer. Parse an explicit list
with `parser.parse_args(["--name", "Ada"])`; this makes tests independent of
the process command line.

- Keep command handling in separate stages:
  - Build the parser.
  - Parse and render.
  - Let `main` return a status code.
- Add bounds with an appropriate parser action or check, distinguish omitted
  options from supplied ones, and let argparse handle invalid input rather than
  printing from helper functions.

## Task

- Build a parser with:
  - The positional `name` argument.
  - The optional `--count` and `--shout` arguments.
- Render the greeting, keep `main(argv)` testable, and restrict count to the
  safe range 1 through 1000.

## Run

```bash
make 01_core_15_command_line_arguments
```

## Further practice

Add an optional `--prefix` argument while keeping the rendering function
independent of `sys.argv`.
