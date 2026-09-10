from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal, TypeGuard

Environment = Literal["development", "test", "production"]


class ConfigError(ValueError):
    pass


@dataclass(frozen=True, slots=True)
class Config:
    service_name: str
    environment: Environment
    port: int
    debug: bool
    database_url: str


def is_environment(value: str) -> TypeGuard[Environment]:
    return value in {"development", "test", "production"}


def load_config(environ: Mapping[str, str]) -> Config:
    required = ("SERVICE_NAME", "ENVIRONMENT", "PORT", "DATABASE_URL")
    missing = [name for name in required if not environ.get(name, "").strip()]
    if missing:
        raise ConfigError(f"missing configuration: {', '.join(missing)}")

    environment = environ["ENVIRONMENT"]
    if not is_environment(environment):
        raise ConfigError("ENVIRONMENT must be development, test, or production")
    try:
        port = int(environ["PORT"])
    except ValueError as error:
        raise ConfigError("PORT must be an integer") from error
    if not 1 <= port <= 65535:
        raise ConfigError("PORT must be between 1 and 65535")

    raw_debug = environ.get("DEBUG", "false").lower()
    if raw_debug not in {"true", "false"}:
        raise ConfigError("DEBUG must be true or false")
    debug = raw_debug == "true"
    if environment == "production" and debug:
        raise ConfigError("DEBUG must be false in production")

    return Config(
        service_name=environ["SERVICE_NAME"].strip(),
        environment=environment,
        port=port,
        debug=debug,
        database_url=environ["DATABASE_URL"],
    )
