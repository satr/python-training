import pytest

from .solution import fibonacci, memoize_int


def test_memoize_int_caches_successful_calls_and_preserves_metadata() -> None:
    calls: list[int] = []

    def double(value: int) -> int:
        """Double one integer."""
        calls.append(value)
        return value * 2

    decorated = memoize_int(double)
    assert decorated(3) == 6
    assert decorated(3) == 6
    assert calls == [3]
    assert decorated.__name__ == "double"
    assert decorated.__doc__ == "Double one integer."


def test_memoize_int_does_not_cache_exceptions() -> None:
    attempts = 0

    def fail_once(value: int) -> int:
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise ValueError("try again")
        return value

    decorated = memoize_int(fail_once)
    with pytest.raises(ValueError, match="try again"):
        decorated(4)
    assert decorated(4) == 4
    assert attempts == 2


@pytest.mark.parametrize(("number", "expected"), [(0, 0), (1, 1), (2, 1), (10, 55)])
def test_fibonacci_values(number: int, expected: int) -> None:
    assert fibonacci(number) == expected


def test_fibonacci_rejects_negative_numbers() -> None:
    with pytest.raises(ValueError, match="negative"):
        fibonacci(-1)
