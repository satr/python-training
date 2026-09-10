import pytest

np = pytest.importorskip("numpy")

from .solution import fit_scaler, transform_features  # noqa: E402


def test_fits_training_data_and_reuses_immutable_parameters() -> None:
    training = np.array([[1.0, 5.0], [3.0, 5.0], [5.0, 5.0]])
    values = np.array([[7.0, 5.0], [9.0, 7.0]])
    training_before = training.copy()
    values_before = values.copy()

    parameters = fit_scaler(training)
    transformed = transform_features(values, parameters)

    assert parameters.mean.tolist() == pytest.approx([3.0, 5.0])
    assert parameters.scale.tolist() == pytest.approx([np.std([1.0, 3.0, 5.0]), 1.0])
    assert transformed[:, 1].tolist() == pytest.approx([0.0, 2.0])
    assert not parameters.mean.flags.writeable
    assert not parameters.scale.flags.writeable
    with pytest.raises(ValueError):
        parameters.mean[0] = 99.0
    assert np.array_equal(training, training_before)
    assert np.array_equal(values, values_before)


def test_transform_does_not_fit_on_later_values() -> None:
    parameters = fit_scaler(np.array([[0.0], [2.0]]))

    transformed = transform_features(np.array([[100.0], [102.0]]), parameters)

    assert transformed[:, 0].tolist() == pytest.approx([99.0, 101.0])


@pytest.mark.parametrize(
    "values",
    [
        np.array([]),
        np.array([1.0, 2.0]),
        np.empty((0, 2)),
        np.array([[1.0, float("nan")]]),
    ],
)
def test_rejects_invalid_matrices(values: object) -> None:
    with pytest.raises(ValueError):
        fit_scaler(values)


def test_rejects_a_different_feature_count() -> None:
    parameters = fit_scaler(np.array([[1.0, 2.0], [3.0, 4.0]]))
    with pytest.raises(ValueError, match="feature count"):
        transform_features(np.array([[1.0, 2.0, 3.0]]), parameters)
