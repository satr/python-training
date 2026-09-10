import pytest

from .solution import (
    Measurement,
    average_temperature,
    parse_measurement,
    valid_temperatures,
)


def test_parse_measurement_strips_fields() -> None:
    assert parse_measurement(" sensor-1, 21.5 ") == Measurement("sensor-1", 21.5)


@pytest.mark.parametrize(
    "row",
    ["", "sensor", ",12", "sensor,nope", "sensor,nan", "sensor,inf", "sensor,-inf"],
)
def test_parse_measurement_rejects_invalid_rows(row: str) -> None:
    with pytest.raises(ValueError):
        parse_measurement(row)


def test_filter_and_average_measurements() -> None:
    values = [Measurement("a", 10), Measurement("b", 20), Measurement("c", 40)]
    assert valid_temperatures(values, 10, 20) == [10, 20]
    assert average_temperature(values) == pytest.approx(70 / 3)
    assert average_temperature([]) is None


def test_temperature_range_is_inclusive_for_generator_input() -> None:
    measurements = (Measurement(str(value), value) for value in [9.0, 10.0, 20.0])
    assert valid_temperatures(measurements, 10.0, 20.0) == [10.0, 20.0]


def test_reversed_temperature_range_is_rejected() -> None:
    with pytest.raises(ValueError, match="minimum"):
        valid_temperatures([], 20.0, 10.0)


def test_average_consumes_one_shot_iterable_once() -> None:
    measurements = (Measurement(str(value), value) for value in [10.0, 20.0])
    assert average_temperature(measurements) == 15.0
    assert list(measurements) == []
