from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SearchResult:
    document_id: str
    score: float


def cosine_similarity(left: list[float], right: list[float]) -> float:
    raise NotImplementedError


def search(
    query: list[float], documents: dict[str, list[float]], *, limit: int
) -> list[SearchResult]:
    raise NotImplementedError

