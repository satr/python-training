from __future__ import annotations


def discounted_prices(
    prices: dict[str, float], percent: float
) -> dict[str, float]:
    raise NotImplementedError


def affordable_items(prices: dict[str, float], maximum: float) -> list[str]:
    raise NotImplementedError
