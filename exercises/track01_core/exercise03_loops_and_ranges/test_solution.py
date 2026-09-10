import pytest

from .solution import project_balances


def test_project_balances_returns_one_balance_per_month() -> None:
    assert project_balances(100.0, 25.0, 3) == [125.0, 150.0, 175.0]


def test_zero_months_returns_empty_projection() -> None:
    assert project_balances(100.0, 25.0, 0) == []


def test_negative_months_are_rejected() -> None:
    with pytest.raises(ValueError, match="months"):
        project_balances(100.0, 25.0, -1)
