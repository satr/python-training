from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass, replace


@dataclass(frozen=True, slots=True)
class Item:
    sku: str
    quantity: int
    unit_price: float
    reorder_level: int = 0


def apply_adjustments(
    inventory: dict[str, Item], adjustments: Iterable[tuple[str, int]]
) -> dict[str, Item]:
    updated = inventory.copy()
    for sku, change in adjustments:
        if sku not in updated:
            raise KeyError(f"unknown SKU: {sku}")
        quantity = updated[sku].quantity + change
        if quantity < 0:
            raise ValueError(f"negative stock for SKU: {sku}")
        updated[sku] = replace(updated[sku], quantity=quantity)
    return updated


def inventory_value(inventory: dict[str, Item]) -> float:
    return sum(item.quantity * item.unit_price for item in inventory.values())


def items_to_reorder(inventory: dict[str, Item]) -> Iterator[Item]:
    for sku in sorted(inventory):
        item = inventory[sku]
        if item.quantity <= item.reorder_level:
            yield item
