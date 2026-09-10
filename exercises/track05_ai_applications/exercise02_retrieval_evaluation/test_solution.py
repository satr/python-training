import pytest

from .solution import Metrics, RetrievalCase, evaluate, macro_average


def test_evaluates_at_k_and_ignores_duplicates() -> None:
    case = RetrievalCase(("x", "x", "a", "b"), frozenset({"a", "c"}))
    assert evaluate(case, k=3) == Metrics(
        precision=pytest.approx(1 / 3),
        recall=pytest.approx(1 / 2),
        reciprocal_rank=pytest.approx(1 / 2),
    )


def test_macro_average() -> None:
    cases = [
        RetrievalCase(("a",), frozenset({"a"})),
        RetrievalCase(("x",), frozenset({"a"})),
    ]
    assert macro_average(cases, k=1) == Metrics(0.5, 0.5, 0.5)


def test_validates_inputs_and_empty_relevance() -> None:
    assert evaluate(RetrievalCase((), frozenset()), k=2) == Metrics(0, 1, 0)
    with pytest.raises(ValueError, match="positive"):
        evaluate(RetrievalCase((), frozenset()), k=0)
    with pytest.raises(ValueError, match="at least one"):
        macro_average([], k=1)
