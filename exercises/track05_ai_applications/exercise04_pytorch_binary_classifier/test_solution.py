from dataclasses import FrozenInstanceError

import pytest

np = pytest.importorskip("numpy")
torch = pytest.importorskip("torch")

from .solution import TrainingResult, train_binary_classifier  # noqa: E402


def test_trains_on_cpu_deterministically_without_mutating_inputs(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    features = np.array([[-2.0], [-1.0], [1.0], [2.0]])
    labels = np.array([0.0, 0.0, 1.0, 1.0])
    features_before = features.copy()
    labels_before = labels.copy()
    observed_devices: list[tuple[str, str]] = []
    original_forward = torch.nn.BCEWithLogitsLoss.forward

    def record_loss_devices(
        loss: torch.nn.BCEWithLogitsLoss,
        inputs: torch.Tensor,
        targets: torch.Tensor,
    ) -> torch.Tensor:
        observed_devices.append((inputs.device.type, targets.device.type))
        return original_forward(loss, inputs, targets)

    monkeypatch.setattr(torch.nn.BCEWithLogitsLoss, "forward", record_loss_devices)

    first = train_binary_classifier(features, labels, epochs=80, learning_rate=0.1)
    second = train_binary_classifier(features, labels, epochs=80, learning_rate=0.1)

    assert observed_devices
    assert set(observed_devices) == {("cpu", "cpu")}
    assert first == second
    assert first.final_loss < first.initial_loss
    assert len(first.probabilities) == len(labels)
    assert all(0.0 <= probability <= 1.0 for probability in first.probabilities)
    assert first.probabilities[0] < 0.5 < first.probabilities[-1]
    assert np.array_equal(features, features_before)
    assert np.array_equal(labels, labels_before)
    with pytest.raises(FrozenInstanceError):
        first.final_loss = 0.0


@pytest.mark.parametrize(
    ("features", "labels"),
    [
        (np.array([]), np.array([])),
        (np.array([1.0, 2.0]), np.array([0.0, 1.0])),
        (np.array([[1.0], [2.0]]), np.array([[0.0], [1.0]])),
        (np.array([[1.0], [2.0]]), np.array([0.0])),
        (np.array([[1.0], [float("inf")]]), np.array([0.0, 1.0])),
        (np.array([[1.0], [2.0]]), np.array([0.0, 2.0])),
    ],
)
def test_rejects_invalid_training_data(features: object, labels: object) -> None:
    with pytest.raises(ValueError):
        train_binary_classifier(features, labels, epochs=10, learning_rate=0.1)


@pytest.mark.parametrize(
    ("epochs", "learning_rate"),
    [(0, 0.1), (-1, 0.1), (10, 0.0), (10, -0.1), (10, float("nan"))],
)
def test_rejects_invalid_hyperparameters(epochs: int, learning_rate: float) -> None:
    with pytest.raises(ValueError):
        train_binary_classifier(
            np.array([[0.0], [1.0]]),
            np.array([0.0, 1.0]),
            epochs=epochs,
            learning_rate=learning_rate,
        )


def test_result_has_an_immutable_probability_sequence() -> None:
    result = TrainingResult(1.0, 0.5, (0.2, 0.8))
    assert isinstance(result.probabilities, tuple)
