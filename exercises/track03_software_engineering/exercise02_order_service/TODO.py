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
        raise NotImplementedError

