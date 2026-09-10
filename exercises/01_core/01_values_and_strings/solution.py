from __future__ import annotations


def calculate_total(quantity: int, unit_price: float) -> float:
    return quantity * unit_price


def format_receipt(item: str, quantity: int, unit_price: float) -> str:
    total = calculate_total(quantity, unit_price)
    return f"{quantity} x {item} @ ${unit_price:.2f} = ${total:.2f}"
