import pytest

from .solution import Order, OrderLine, OrderService


class InMemoryOrders:
    def __init__(self) -> None:
        self.orders: dict[str, Order] = {}
        self.save_calls = 0

    def get(self, order_id: str) -> Order | None:
        return self.orders.get(order_id)

    def save(self, order: Order) -> None:
        self.save_calls += 1
        self.orders[order.order_id] = order


def test_places_and_persists_order() -> None:
    repository = InMemoryOrders()
    order = OrderService(repository).place_order(
        "order-1", [OrderLine("book", 2, 12.5), OrderLine("pen", 3, 1.0)]
    )
    assert order.total == 28.0
    assert repository.orders["order-1"] == order
    assert repository.save_calls == 1


def test_rejects_duplicate_without_saving() -> None:
    repository = InMemoryOrders()
    service = OrderService(repository)
    service.place_order("order-1", [OrderLine("book", 1, 10)])
    with pytest.raises(ValueError, match="already exists"):
        service.place_order("order-1", [OrderLine("book", 1, 10)])
    assert repository.save_calls == 1


@pytest.mark.parametrize("lines", [[], [OrderLine("book", 0, 10)]])
def test_rejects_invalid_lines(lines: list[OrderLine]) -> None:
    with pytest.raises(ValueError):
        OrderService(InMemoryOrders()).place_order("order-1", lines)
