from __future__ import annotations

from collections.abc import Callable


def memoize_int(function: Callable[[int], int]) -> Callable[[int], int]:
    raise NotImplementedError


def fibonacci(number: int) -> int:
    raise NotImplementedError
