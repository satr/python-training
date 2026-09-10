from __future__ import annotations

from collections.abc import Callable, Iterable
from concurrent.futures import ThreadPoolExecutor
from typing import TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


def bounded_map(
    function: Callable[[InputT], OutputT],
    values: Iterable[InputT],
    *,
    max_workers: int,
) -> list[OutputT]:
    if max_workers < 1:
        raise ValueError("max_workers must be positive")
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(function, values))
