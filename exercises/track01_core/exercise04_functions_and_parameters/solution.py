from __future__ import annotations


def percentage(amount: float, rate: float) -> float:
    return amount * rate / 100.0


def split_bill(subtotal: float, tip_percent: float = 15.0, *, people: int = 1) -> float:
    if people <= 0:
        raise ValueError("people must be positive")
    total = subtotal + percentage(subtotal, tip_percent)
    return total / people
