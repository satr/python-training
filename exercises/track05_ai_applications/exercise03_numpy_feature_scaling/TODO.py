from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]


@dataclass(frozen=True, slots=True)
class ScalingParameters:
    mean: FloatArray
    scale: FloatArray

    def __post_init__(self) -> None:
        raise NotImplementedError


def fit_scaler(training: npt.ArrayLike) -> ScalingParameters:
    raise NotImplementedError


def transform_features(
    values: npt.ArrayLike, parameters: ScalingParameters
) -> FloatArray:
    raise NotImplementedError
