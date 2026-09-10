from __future__ import annotations


def percentage(amount: float, rate: float) -> float:
    raise NotImplementedError


def split_bill(
    subtotal: float, tip_percent: float = 15.0, *, people: int = 1
) -> float:
    raise NotImplementedError
