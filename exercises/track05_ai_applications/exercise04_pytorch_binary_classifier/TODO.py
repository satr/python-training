from __future__ import annotations

from dataclasses import dataclass

import numpy.typing as npt


@dataclass(frozen=True, slots=True)
class TrainingResult:
    initial_loss: float
    final_loss: float
    probabilities: tuple[float, ...]


def train_binary_classifier(
    features: npt.ArrayLike,
    labels: npt.ArrayLike,
    *,
    epochs: int,
    learning_rate: float,
) -> TrainingResult:
    raise NotImplementedError
