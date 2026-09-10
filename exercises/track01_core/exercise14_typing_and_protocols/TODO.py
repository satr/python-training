from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import Protocol, TypeVar

T = TypeVar("T")


def first_matching(
    items: Iterable[T], predicate: Callable[[T], bool]
) -> T | None:
    raise NotImplementedError


class Describable(Protocol):
    def describe(self) -> str:
        raise NotImplementedError


def describe_all(items: Iterable[Describable]) -> list[str]:
    raise NotImplementedError
