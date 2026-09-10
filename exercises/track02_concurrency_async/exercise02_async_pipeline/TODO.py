from __future__ import annotations

from collections.abc import Awaitable, Callable, Iterable
from typing import TypeVar

InputT = TypeVar("InputT")
OutputT = TypeVar("OutputT")


async def run_pipeline(
    values: Iterable[InputT],
    transform: Callable[[InputT], Awaitable[OutputT]],
    *,
    workers: int,
    queue_size: int,
) -> list[OutputT]:
    raise NotImplementedError

