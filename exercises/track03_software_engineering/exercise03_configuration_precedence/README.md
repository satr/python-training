# Configuration precedence

## Theory

Configuration commonly has several sources. Merge them in a documented order:
safe defaults first, environment variables second, and explicit programmatic
overrides last. Validate and convert values at the boundary.

## Learn before coding

- Represent precedence explicitly:
  - Start with a default such as `port = 8000`.
  - Replace it when an environment key is present.
  - Replace it again when an override contains that key.

Convert environment text with `int("9000")`, but accept an already-typed
override only after checking its type. For example, a `debug` override should
win over an environment `"false"`.

- Once precedence is resolved:
  - Validate the winning value once.
  - Reject unknown keys and non-finite numeric values.
  - Avoid mutating either input mapping.

## Task

- Implement `load_config` for `host`, `port`, `debug`, and `timeout`.
- Resolve each source in precedence order:
  - Use defaults of `localhost`, `8000`, `false`, and `5.0`.
  - Read `APP_HOST`, `APP_PORT`, `APP_DEBUG`, and `APP_TIMEOUT`.
  - Apply explicit field-name overrides last.
- Return a typed `Config` and raise `ConfigError` for unknown or invalid values.
- Require finite, positive timeouts; reject NaN and infinity.

## Run

```bash
make 03_software_engineering_03_configuration_precedence
```

## Further practice

Add a configuration file source between defaults and the environment without
changing the precedence contract.
