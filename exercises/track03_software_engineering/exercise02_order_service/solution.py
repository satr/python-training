from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True, slots=True)
class OrderLine:
    sku: str
    quantity: int
    unit_price: float


@dataclass(frozen=True, slots=True)
class Order:
    order_id: str
    lines: tuple[OrderLine, ...]
    total: float


class OrderRepository(Protocol):
    def get(self, order_id: str) -> Order | None: ...

    def save(self, order: Order) -> None: ...


class OrderService:
    def __init__(self, repository: OrderRepository) -> None:
        self._repository = repository

    def place_order(self, order_id: str, lines: list[OrderLine]) -> Order:
        if not order_id.strip():
            raise ValueError("order_id must not be empty")
        if not lines:
            raise ValueError("an order needs at least one line")
        if self._repository.get(order_id) is not None:
            raise ValueError(f"order already exists: {order_id}")
        if any(line.quantity <= 0 or line.unit_price < 0 for line in lines):
            raise ValueError("quantity must be positive and price non-negative")

        immutable_lines = tuple(lines)
        total = sum(line.quantity * line.unit_price for line in immutable_lines)
        order = Order(order_id, immutable_lines, total)
        self._repository.save(order)
        return order
