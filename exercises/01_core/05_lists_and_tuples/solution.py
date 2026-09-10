from __future__ import annotations


def summarize_scores(scores: list[int]) -> tuple[int, int, float] | None:
    if not scores:
        return None
    return min(scores), max(scores), sum(scores) / len(scores)


def top_scores(scores: list[int], limit: int = 3) -> list[int]:
    if limit <= 0:
        return []
    return sorted(scores, reverse=True)[:limit]
