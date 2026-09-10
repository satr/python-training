from __future__ import annotations


def count_items(items: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts


def common_items(left: set[str], right: set[str]) -> list[str]:
    return sorted(left & right)
