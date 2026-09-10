from __future__ import annotations

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


def load_config(
    environ: Mapping[str, str],
    overrides: Mapping[str, object] | None = None,
) -> Config:
    raise NotImplementedError
