import asyncio

import pytest

from .solution import run_pipeline


def test_pipeline_preserves_order() -> None:
    active = 0
    peak = 0

    async def transform(value: int) -> int:
        nonlocal active, peak
        active += 1
        peak = max(peak, active)
        await asyncio.sleep((4 - value) * 0.002)
        active -= 1
        return value * 10

    result = asyncio.run(run_pipeline(range(5), transform, workers=3, queue_size=2))
    assert result == [0, 10, 20, 30, 40]
    assert 1 < peak <= 3


def test_pipeline_validates_limits() -> None:
    async def identity(value: int) -> int:
        return value

    with pytest.raises(ValueError, match="positive"):
        asyncio.run(run_pipeline([1], identity, workers=0, queue_size=1))
