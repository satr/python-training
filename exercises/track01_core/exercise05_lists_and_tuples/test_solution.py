from .solution import summarize_scores, top_scores


def test_summarize_scores_returns_minimum_maximum_and_average() -> None:
    assert summarize_scores([8, 10, 6]) == (6, 10, 8.0)


def test_empty_scores_have_no_summary() -> None:
    assert summarize_scores([]) is None


def test_top_scores_are_descending_without_mutating_input() -> None:
    scores = [7, 10, 8, 10]
    assert top_scores(scores) == [10, 10, 8]
    assert scores == [7, 10, 8, 10]


def test_non_positive_limit_returns_empty_list() -> None:
    assert top_scores([10, 8], 0) == []
