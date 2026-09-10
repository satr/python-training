from __future__ import annotations

import math
from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Measurement:
    sensor_id: str
    celsius: float


def parse_measurement(row: str) -> Measurement:
    parts = [part.strip() for part in row.split(",")]
    if len(parts) != 2:
        raise ValueError("measurement must have sensor_id,celsius")
    sensor_id, raw_celsius = parts
    if not sensor_id:
        raise ValueError("sensor_id must not be empty")
    try:
        celsius = float(raw_celsius)
    except ValueError as error:
        raise ValueError("celsius must be a number") from error
    if not math.isfinite(celsius):
        raise ValueError("celsius must be finite")
    return Measurement(sensor_id=sensor_id, celsius=celsius)


def valid_temperatures(
    measurements: Iterable[Measurement], minimum: float, maximum: float
) -> list[float]:
    if minimum > maximum:
        raise ValueError("minimum must not exceed maximum")
    return [
        measurement.celsius
        for measurement in measurements
        if minimum <= measurement.celsius <= maximum
    ]


def average_temperature(measurements: Iterable[Measurement]) -> float | None:
    temperatures = [measurement.celsius for measurement in measurements]
    return sum(temperatures) / len(temperatures) if temperatures else None
