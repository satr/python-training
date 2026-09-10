import pytest

from .solution import delivery_fee


@pytest.mark.parametrize(
    ("order_total", "is_member"),
    [(50.0, False), (75.0, False), (10.0, True)],
)
def test_qualifying_orders_have_free_delivery(
    order_total: float, is_member: bool
) -> None:
    assert delivery_fee(order_total, 20.0, is_member) == 0.0


def test_standard_fee_applies_through_five_kilometres() -> None:
    assert delivery_fee(49.99, 5.0) == 5.0


def test_distance_surcharge_applies_beyond_five_kilometres() -> None:
    assert delivery_fee(20.0, 7.0) == 8.0
