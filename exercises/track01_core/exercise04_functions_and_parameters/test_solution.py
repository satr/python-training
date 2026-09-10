import pytest

from .solution import percentage, split_bill


def test_percentage_calculates_part_of_amount() -> None:
    assert percentage(80.0, 12.5) == 10.0


def test_split_bill_uses_default_tip_and_people() -> None:
    assert split_bill(100.0) == 115.0


def test_split_bill_accepts_custom_tip_and_keyword_only_people() -> None:
    assert split_bill(100.0, 20.0, people=4) == 30.0


def test_split_bill_rejects_non_positive_people() -> None:
    with pytest.raises(ValueError, match="people"):
        split_bill(100.0, people=0)
