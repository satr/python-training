from .solution import calculate_total, format_receipt


def test_calculate_total_multiplies_quantity_and_price() -> None:
    assert calculate_total(3, 2.5) == 7.5


def test_format_receipt_uses_fixed_two_decimal_places() -> None:
    assert format_receipt("notebook", 3, 2.5) == ("3 x notebook @ $2.50 = $7.50")


def test_format_receipt_uses_calculated_total() -> None:
    assert format_receipt("pen", 2, 1.235) == "2 x pen @ $1.24 = $2.47"
