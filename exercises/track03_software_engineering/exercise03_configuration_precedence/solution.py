from __future__ import annotations

import math
from collections.abc import Mapping
from dataclasses import dataclass


class ConfigError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class Config:
    host: str
    port: int
    debug: bool
    timeout: float


DEFAULTS: dict[str, object] = {
    "host": "localhost",
    "port": 8000,
    "debug": False,
    "timeout": 5.0,
}
ENVIRONMENT_KEYS = {
    "host": "APP_HOST",
    "port": "APP_PORT",
    "debug": "APP_DEBUG",
    "timeout": "APP_TIMEOUT",
}


def _as_bool(value: object) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str) and value.lower() in {"true", "false"}:
        return value.lower() == "true"
    raise ConfigError("debug must be true or false")


def _load_value(name: str, value: object) -> object:
    try:
        if name == "host":
            if not isinstance(value, str) or not value.strip():
                raise ConfigError("host must not be empty")
            return value.strip()
        if name == "port":
            if isinstance(value, bool) or not isinstance(value, (int, str)):
                raise ConfigError("port has an invalid value")
            parsed = int(value)
            if not 1 <= parsed <= 65535:
                raise ConfigError("port must be between 1 and 65535")
            return parsed
        if name == "debug":
            return _as_bool(value)
        if isinstance(value, bool) or not isinstance(value, (int, float, str)):
            raise ConfigError("timeout has an invalid value")
        parsed_timeout = float(value)
        if not math.isfinite(parsed_timeout) or parsed_timeout <= 0:
            raise ConfigError("timeout must be finite and positive")
        return parsed_timeout
    except (TypeError, ValueError) as error:
        raise ConfigError(f"{name} has an invalid value") from error


def load_config(
    environ: Mapping[str, str],
    overrides: Mapping[str, object] | None = None,
) -> Config:
    values = dict(DEFAULTS)
    for name, environment_key in ENVIRONMENT_KEYS.items():
        if environment_key in environ:
            values[name] = environ[environment_key]
    if overrides:
        unknown = set(overrides) - set(DEFAULTS)
        if unknown:
            raise ConfigError(f"unknown configuration: {', '.join(sorted(unknown))}")
        values.update(overrides)
    typed = {name: _load_value(name, value) for name, value in values.items()}
    return Config(
        host=typed["host"],  # type: ignore[arg-type]
        port=typed["port"],  # type: ignore[arg-type]
        debug=typed["debug"],  # type: ignore[arg-type]
        timeout=typed["timeout"],  # type: ignore[arg-type]
    )
