from __future__ import annotations

import asyncio
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
    if workers < 1 or queue_size < 1:
        raise ValueError("workers and queue_size must be positive")

    queue: asyncio.Queue[tuple[int, InputT] | None] = asyncio.Queue(queue_size)
    results: dict[int, OutputT] = {}

    async def worker() -> None:
        while True:
            item = await queue.get()
            try:
                if item is None:
                    return
                index, value = item
                results[index] = await transform(value)
            finally:
                queue.task_done()

    async with asyncio.TaskGroup() as group:
        for _ in range(workers):
            group.create_task(worker())
        for indexed_value in enumerate(values):
            await queue.put(indexed_value)
        for _ in range(workers):
            await queue.put(None)
        await queue.join()

    return [results[index] for index in range(len(results))]
