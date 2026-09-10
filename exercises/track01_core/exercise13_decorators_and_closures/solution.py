from __future__ import annotations

from collections.abc import Callable
from functools import wraps
from typing import cast


def memoize_int(function: Callable[[int], int]) -> Callable[[int], int]:
    cache: dict[int, int] = {}

    @wraps(function)
    def wrapper(value: int) -> int:
        if value not in cache:
            result = function(value)
            cache[value] = result
        return cache[value]

    return cast(Callable[[int], int], wrapper)


@memoize_int
def fibonacci(number: int) -> int:
    if number < 0:
        raise ValueError("number must not be negative")
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)
