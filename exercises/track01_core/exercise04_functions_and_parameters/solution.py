from __future__ import annotations


def percentage(amount: float, rate: float) -> float:
    return amount * rate / 100.0


def split_bill(
    subtotal: float,
    tip_percent: float = 15.0,
    *,
    people: int = 1,
    discount_percent: float = 0.0,
) -> float:
    if people <= 0:
        raise ValueError("people must be positive")
    if not 0.0 <= discount_percent <= 100.0:
        raise ValueError("discount_percent must be between 0 and 100")
    discounted_subtotal = subtotal - percentage(subtotal, discount_percent)
    total = discounted_subtotal + percentage(discounted_subtotal, tip_percent)
    return total / people
