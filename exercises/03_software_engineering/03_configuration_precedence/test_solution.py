import pytest

from .solution import Config, ConfigError, load_config


def test_defaults_are_used_when_sources_are_empty() -> None:
    assert load_config({}) == Config("localhost", 8000, False, 5.0)


def test_environment_overrides_defaults() -> None:
    config = load_config(
        {"APP_HOST": "example.test", "APP_PORT": "9000", "APP_DEBUG": "true"}
    )

    assert config == Config("example.test", 9000, True, 5.0)


def test_explicit_overrides_take_precedence_and_are_typed() -> None:
    config = load_config(
        {"APP_PORT": "9000", "APP_DEBUG": "false"},
        {"port": 9100, "debug": True, "timeout": "2.5"},
    )

    assert config == Config("localhost", 9100, True, 2.5)


@pytest.mark.parametrize(
    ("environ", "overrides", "message"),
    [
        ({"APP_PORT": "not-a-port"}, None, "port"),
        ({"APP_DEBUG": "sometimes"}, None, "debug"),
        ({}, {"timeout": 0}, "timeout"),
        ({"APP_TIMEOUT": "nan"}, None, "timeout"),
        ({}, {"timeout": float("inf")}, "timeout"),
    ],
)
def test_invalid_values_raise_actionable_errors(
    environ: dict[str, str], overrides: dict[str, object] | None, message: str
) -> None:
    with pytest.raises(ConfigError, match=message):
        load_config(environ, overrides)
