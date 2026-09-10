import pytest

from .solution import cosine_similarity, search


def test_cosine_similarity() -> None:
    assert cosine_similarity([1, 0], [1, 0]) == pytest.approx(1)
    assert cosine_similarity([1, 0], [0, 1]) == pytest.approx(0)
    with pytest.raises(ValueError):
        cosine_similarity([0, 0], [1, 0])


def test_search_ranks_and_breaks_ties() -> None:
    results = search(
        [1, 0],
        {"z": [0, 1], "b": [1, 1], "a": [1, 1], "best": [2, 0]},
        limit=3,
    )
    assert [result.document_id for result in results] == ["best", "a", "b"]


def test_search_validates_limit() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        search([1], {"a": [1]}, limit=-1)
