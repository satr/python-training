import pytest

from .solution import main, parse_arguments, render_greeting


def test_parse_arguments_supports_positional_and_optional_values() -> None:
    arguments = parse_arguments(["Ada", "--count", "2", "--shout"])

    assert arguments.name == "Ada"
    assert arguments.count == 2
    assert arguments.shout is True


def test_render_greeting_uses_defaults() -> None:
    assert render_greeting(parse_arguments(["Ada"])) == "Hello, Ada!"


def test_main_accepts_explicit_argv(capsys: pytest.CaptureFixture[str]) -> None:
    assert main(["Lin", "--count", "2"]) == 0
    assert capsys.readouterr().out == "Hello, Lin!\nHello, Lin!\n"


@pytest.mark.parametrize("count", ["0", "1001"])
def test_parse_arguments_rejects_count_outside_safe_range(count: str) -> None:
    with pytest.raises(SystemExit):
        parse_arguments(["Ada", "--count", count])
