import pytest

from .solution import percentage, split_bill


def test_percentage_calculates_part_of_amount() -> None:
    assert percentage(80.0, 12.5) == 10.0


def test_split_bill_uses_default_tip_and_people() -> None:
    assert split_bill(100.0) == 115.0


def test_split_bill_accepts_custom_tip_and_keyword_only_people() -> None:
    assert split_bill(100.0, 20.0, people=4) == 30.0


def test_split_bill_applies_optional_discount_before_tip() -> None:
    assert split_bill(100.0, discount_percent=10.0) == 103.5


def test_split_bill_rejects_non_positive_people() -> None:
    with pytest.raises(ValueError, match="people"):
        split_bill(100.0, people=0)


def test_split_bill_rejects_invalid_discount() -> None:
    with pytest.raises(ValueError, match="discount_percent"):
        split_bill(100.0, discount_percent=101.0)
