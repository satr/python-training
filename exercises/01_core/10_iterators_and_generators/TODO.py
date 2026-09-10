from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    sku: str
    quantity: int
    unit_price: float
    reorder_level: int = 0


def apply_adjustments(
    inventory: dict[str, Item], adjustments: Iterable[tuple[str, int]]
) -> dict[str, Item]:
    raise NotImplementedError


def inventory_value(inventory: dict[str, Item]) -> float:
    raise NotImplementedError


def items_to_reorder(inventory: dict[str, Item]) -> Iterator[Item]:
    raise NotImplementedError

