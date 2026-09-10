from __future__ import annotations

from collections.abc import Callable, Iterable
from typing import TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


def bounded_map(
    function: Callable[[InputT], OutputT],
    values: Iterable[InputT],
    *,
    max_workers: int,
) -> list[OutputT]:
    raise NotImplementedError

