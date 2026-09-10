from .solution import common_items, count_items


def test_count_items_preserves_first_seen_key_order() -> None:
    assert count_items(["pear", "apple", "pear"]) == {"pear": 2, "apple": 1}


def test_count_items_handles_empty_input() -> None:
    assert count_items([]) == {}


def test_common_items_returns_sorted_intersection() -> None:
    assert common_items({"pear", "apple", "plum"}, {"plum", "pear"}) == [
        "pear",
        "plum",
    ]
