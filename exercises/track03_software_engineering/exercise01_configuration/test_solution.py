import pytest

from .solution import Config, ConfigError, load_config

VALID_ENV = {
    "SERVICE_NAME": "orders",
    "ENVIRONMENT": "test",
    "PORT": "8080",
    "DATABASE_URL": "sqlite:///:memory:",
}


def test_loads_typed_config_with_defaults() -> None:
    assert load_config(VALID_ENV) == Config(
        "orders", "test", 8080, False, "sqlite:///:memory:"
    )


@pytest.mark.parametrize(
    ("updates", "message"),
    [
        ({"PORT": "zero"}, "integer"),
        ({"PORT": "70000"}, "between"),
        ({"DEBUG": "yes"}, "true or false"),
        ({"ENVIRONMENT": "production", "DEBUG": "true"}, "production"),
    ],
)
def test_rejects_invalid_configuration(updates: dict[str, str], message: str) -> None:
    with pytest.raises(ConfigError, match=message):
        load_config(VALID_ENV | updates)


def test_reports_missing_keys() -> None:
    with pytest.raises(ConfigError, match="DATABASE_URL"):
        load_config(
            {key: value for key, value in VALID_ENV.items() if key != "DATABASE_URL"}
        )
