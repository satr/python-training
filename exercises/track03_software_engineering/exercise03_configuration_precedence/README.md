# Configuration precedence

## Theory

Configuration commonly has several sources. Merge them in a documented order:
safe defaults first, environment variables second, and explicit programmatic
overrides last. Validate and convert values at the boundary.

## Learn before coding

Represent precedence explicitly: start with a default such as `port = 8000`,
replace it when an environment key is present, then replace it when an
override contains that key. Convert environment text with `int("9000")`, but
accept the already-typed override value only after checking its type. For
example, an override for `debug` should win over an environment `"false"`.
Choose the winning value first, validate it once, reject unknown keys and
non-finite numeric values, and avoid mutating either input mapping.

## Task

Implement `load_config` for `host`, `port`, `debug`, and `timeout`. Use defaults
of `localhost`, `8000`, `false`, and `5.0`; read `APP_HOST`, `APP_PORT`,
`APP_DEBUG`, and `APP_TIMEOUT`; then apply explicit field-name overrides.
Return a typed `Config` and raise `ConfigError` for unknown or invalid values.
Timeouts must be finite and positive; NaN and infinity are rejected.

## Run

```bash
make 03_software_engineering_03_configuration_precedence
```

## Further practice

Add a configuration file source between defaults and the environment without
changing the precedence contract.
