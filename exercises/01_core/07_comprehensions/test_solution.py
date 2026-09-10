from .solution import affordable_items, discounted_prices


def test_discounted_prices_returns_new_dictionary() -> None:
    prices = {"book": 20.0, "pen": 2.0}
    discounted = discounted_prices(prices, 25.0)
    assert discounted == {"book": 15.0, "pen": 1.5}
    assert prices == {"book": 20.0, "pen": 2.0}
    assert discounted is not prices


def test_affordable_items_includes_maximum_and_sorts_names() -> None:
    prices = {"pen": 2.0, "book": 20.0, "pad": 5.0}
    assert affordable_items(prices, 5.0) == ["pad", "pen"]
