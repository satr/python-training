from __future__ import annotations


def discounted_prices(prices: dict[str, float], percent: float) -> dict[str, float]:
    multiplier = 1.0 - percent / 100.0
    return {name: price * multiplier for name, price in prices.items()}


def affordable_items(prices: dict[str, float], maximum: float) -> list[str]:
    return sorted(name for name, price in prices.items() if price <= maximum)
