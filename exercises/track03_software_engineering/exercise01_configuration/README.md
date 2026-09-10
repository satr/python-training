# Configuration

## Theory

Configuration enters a program as strings. Parse it once at the boundary into
a typed object, validate cross-field constraints, and never log secrets.

## Task

Implement `load_config` for service name, environment, port, debug mode, and
database URL. Produce actionable `ConfigError` messages.

## Run

```bash
make 03_software_engineering_01_configuration
```

## Further practice

Layer defaults, a file, environment variables, and command-line overrides.
