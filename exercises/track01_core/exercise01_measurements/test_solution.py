import pytest

from .solution import (
    Measurement,
    average_temperature,
    parse_measurement,
    valid_temperatures,
)


def test_parse_measurement_strips_fields() -> None:
    assert parse_measurement(" sensor-1, 21.5 ") == Measurement("sensor-1", 21.5)


@pytest.mark.parametrize("row", ["", "sensor", ",12", "sensor,nope", "sensor,nan"])
def test_parse_measurement_rejects_invalid_rows(row: str) -> None:
    with pytest.raises(ValueError):
        parse_measurement(row)


def test_filter_and_average_measurements() -> None:
    values = [Measurement("a", 10), Measurement("b", 20), Measurement("c", 40)]
    assert valid_temperatures(values, 10, 20) == [10, 20]
    assert average_temperature(values) == pytest.approx(70 / 3)
    assert average_temperature([]) is None
