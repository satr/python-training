from dataclasses import dataclass

from .solution import describe_all, first_matching


def test_first_matching_returns_first_value_without_over_consuming() -> None:
    items = iter([1, 4, 6])
    assert first_matching(items, lambda value: value % 2 == 0) == 4
    assert next(items) == 6


def test_first_matching_returns_none_when_no_value_matches() -> None:
    assert first_matching(["one", "two"], lambda value: len(value) > 3) is None


@dataclass
class Product:
    name: str

    def describe(self) -> str:
        return f"Product: {self.name}"


class Status:
    def describe(self) -> str:
        return "Status: ready"


def test_describe_all_accepts_structurally_compatible_objects() -> None:
    assert describe_all([Product("book"), Status()]) == [
        "Product: book",
        "Status: ready",
    ]
