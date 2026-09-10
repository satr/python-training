from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SearchResult:
    document_id: str
    score: float


def cosine_similarity(left: list[float], right: list[float]) -> float:
    if not left or len(left) != len(right):
        raise ValueError("vectors must be non-empty and have equal dimensions")
    left_norm = math.sqrt(sum(value * value for value in left))
    right_norm = math.sqrt(sum(value * value for value in right))
    if left_norm == 0 or right_norm == 0:
        raise ValueError("zero vectors have no cosine similarity")
    return sum(a * b for a, b in zip(left, right, strict=True)) / (
        left_norm * right_norm
    )


def search(
    query: list[float], documents: dict[str, list[float]], *, limit: int
) -> list[SearchResult]:
    if limit < 0:
        raise ValueError("limit must be non-negative")
    ranked = [
        SearchResult(document_id, cosine_similarity(query, embedding))
        for document_id, embedding in documents.items()
    ]
    ranked.sort(key=lambda result: (-result.score, result.document_id))
    return ranked[:limit]
