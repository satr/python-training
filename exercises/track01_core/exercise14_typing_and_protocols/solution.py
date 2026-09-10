from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Protocol, TypeVar

T = TypeVar("T")


def first_matching(items: Iterable[T], predicate: Callable[[T], bool]) -> T | None:
    for item in items:
        if predicate(item):
            return item
    return None


class Describable(Protocol):
    def describe(self) -> str: ...


def describe_all(items: Iterable[Describable]) -> list[str]:
    return [item.describe() for item in items]
