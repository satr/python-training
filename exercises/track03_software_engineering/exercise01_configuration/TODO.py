from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Literal

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


def load_config(environ: Mapping[str, str]) -> Config:
    raise NotImplementedError

