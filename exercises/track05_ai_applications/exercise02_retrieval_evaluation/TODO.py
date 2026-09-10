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
    raise NotImplementedError


def macro_average(cases: Iterable[RetrievalCase], *, k: int) -> Metrics:
    raise NotImplementedError

