from __future__ import annotations


def summarize_scores(scores: list[int]) -> tuple[int, int, float] | None:
    raise NotImplementedError


def top_scores(scores: list[int], limit: int = 3) -> list[int]:
    raise NotImplementedError
