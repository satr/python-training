from __future__ import annotations

import math
from dataclasses import dataclass
from numbers import Integral, Real

import numpy as np
import numpy.typing as npt
import torch


@dataclass(frozen=True, slots=True)
class TrainingResult:
    initial_loss: float
    final_loss: float
    probabilities: tuple[float, ...]


def _numeric_array(values: npt.ArrayLike, *, name: str) -> npt.NDArray[np.float64]:
    raw = np.asarray(values)
    if raw.dtype.kind not in "iufb":
        raise ValueError(f"{name} must contain real numeric values")
    result = raw.astype(np.float64, copy=True)
    if not np.isfinite(result).all():
        raise ValueError(f"{name} must contain only finite values")
    return result


def train_binary_classifier(
    features: npt.ArrayLike,
    labels: npt.ArrayLike,
    *,
    epochs: int,
    learning_rate: float,
) -> TrainingResult:
    feature_array = _numeric_array(features, name="features")
    label_array = _numeric_array(labels, name="labels")
    if (
        feature_array.ndim != 2
        or not feature_array.shape[0]
        or not feature_array.shape[1]
    ):
        raise ValueError("features must be a non-empty two-dimensional matrix")
    if label_array.ndim != 1:
        raise ValueError("labels must be one-dimensional")
    if label_array.shape[0] != feature_array.shape[0]:
        raise ValueError("features and labels must have matching rows")
    if not np.isin(label_array, (0.0, 1.0)).all():
        raise ValueError("labels must be binary")
    if isinstance(epochs, bool) or not isinstance(epochs, Integral) or epochs <= 0:
        raise ValueError("epochs must be a positive integer")
    if (
        isinstance(learning_rate, bool)
        or not isinstance(learning_rate, Real)
        or not math.isfinite(float(learning_rate))
        or learning_rate <= 0
    ):
        raise ValueError("learning_rate must be positive and finite")

    inputs = torch.tensor(feature_array, dtype=torch.float64, device="cpu")
    targets = torch.tensor(label_array, dtype=torch.float64, device="cpu").reshape(
        -1, 1
    )
    weights = torch.nn.Parameter(
        torch.zeros((feature_array.shape[1], 1), dtype=torch.float64, device="cpu")
    )
    bias = torch.nn.Parameter(torch.zeros(1, dtype=torch.float64, device="cpu"))
    criterion = torch.nn.BCEWithLogitsLoss()
    optimizer = torch.optim.SGD([weights, bias], lr=float(learning_rate))

    initial_loss = float(criterion(inputs @ weights + bias, targets).item())
    for _ in range(int(epochs)):
        optimizer.zero_grad()
        loss = criterion(inputs @ weights + bias, targets)
        loss.backward()
        optimizer.step()

    with torch.no_grad():
        logits = inputs @ weights + bias
        final_loss = float(criterion(logits, targets).item())
        probabilities = tuple(float(value) for value in torch.sigmoid(logits).flatten())
    return TrainingResult(initial_loss, final_loss, probabilities)
