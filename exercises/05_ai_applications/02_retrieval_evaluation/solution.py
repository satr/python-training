from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RetrievalCase:
    retrieved: tuple[str, ...]
    relevant: frozenset[str]


@dataclass(frozen=True, slots=True)
class Metrics:
    precision: float
    recall: float
    reciprocal_rank: float


def evaluate(case: RetrievalCase, *, k: int) -> Metrics:
    if k < 1:
        raise ValueError("k must be positive")
    seen: set[str] = set()
    ranking: list[str] = []
    for document_id in case.retrieved:
        if document_id not in seen:
            ranking.append(document_id)
            seen.add(document_id)
        if len(ranking) == k:
            break
    relevant_retrieved = [item for item in ranking if item in case.relevant]
    precision = len(relevant_retrieved) / k
    recall = len(relevant_retrieved) / len(case.relevant) if case.relevant else 1.0
    reciprocal_rank = next(
        (
            1 / rank
            for rank, item in enumerate(ranking, start=1)
            if item in case.relevant
        ),
        0.0,
    )
    return Metrics(precision, recall, reciprocal_rank)


def macro_average(cases: Iterable[RetrievalCase], *, k: int) -> Metrics:
    results = [evaluate(case, k=k) for case in cases]
    if not results:
        raise ValueError("at least one evaluation case is required")
    count = len(results)
    return Metrics(
        sum(result.precision for result in results) / count,
        sum(result.recall for result in results) / count,
        sum(result.reciprocal_rank for result in results) / count,
    )
