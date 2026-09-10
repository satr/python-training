import pytest

from .solution import Item, apply_adjustments, inventory_value, items_to_reorder


def test_adjustments_return_new_inventory() -> None:
    original = {"b": Item("b", 2, 3.5), "a": Item("a", 1, 2.0, 1)}
    updated = apply_adjustments(original, [("b", 3)])
    assert updated["b"].quantity == 5
    assert original["b"].quantity == 2


def test_adjustments_validate_stock() -> None:
    inventory = {"a": Item("a", 1, 2.0)}
    with pytest.raises(KeyError, match="unknown SKU"):
        apply_adjustments(inventory, [("missing", 1)])
    with pytest.raises(ValueError, match="negative stock"):
        apply_adjustments(inventory, [("a", -2)])


def test_value_and_reorder_are_deterministic() -> None:
    inventory = {
        "b": Item("b", 2, 3.5, 2),
        "a": Item("a", 1, 2.0, 0),
        "c": Item("c", 0, 10.0, 1),
    }
    assert inventory_value(inventory) == 9.0
    assert [item.sku for item in items_to_reorder(inventory)] == ["b", "c"]
