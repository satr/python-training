from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Measurement:
    sensor_id: str
    celsius: float


def parse_measurement(row: str) -> Measurement:
    raise NotImplementedError


def valid_temperatures(
    measurements: Iterable[Measurement], minimum: float, maximum: float
) -> list[float]:
    raise NotImplementedError


def average_temperature(measurements: Iterable[Measurement]) -> float | None:
    raise NotImplementedError

