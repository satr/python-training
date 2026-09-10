# Configuration

## Theory

Configuration enters a program as strings. Parse it once at the boundary into
a typed object, validate cross-field constraints, and never log secrets.

## Learn before coding

Environment mappings contain strings: `int("8080")` creates a port number and
`value.lower() in {"1", "true", "yes"}` can recognize a boolean spelling.

- Build the typed dataclass only after preparation succeeds:
  - Read defaults and require fields.
  - Parse each value.
  - Validate allowed environments, ranges, and cross-field rules.
  - Return `Config`.

For example, parse `"120"` as a timeout-like integer before comparing it.
Reject unknown boolean spellings, and keep exception messages useful without
including sensitive configuration values.

## Task

- Implement `load_config` for service name, environment, port, debug mode, and
  database URL.
- Produce actionable `ConfigError` messages.

## Run

```bash
make 03_software_engineering_01_configuration
```

## Further practice

Layer defaults, a file, environment variables, and command-line overrides.
