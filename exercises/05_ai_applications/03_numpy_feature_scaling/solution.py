from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import numpy.typing as npt

FloatArray = npt.NDArray[np.float64]


def _as_finite_matrix(values: npt.ArrayLike, *, name: str) -> FloatArray:
    raw = np.asarray(values)
    if raw.dtype.kind not in "iuf":
        raise ValueError(f"{name} must contain real numeric values")
    matrix = raw.astype(np.float64, copy=True)
    if matrix.ndim != 2 or not matrix.shape[0] or not matrix.shape[1]:
        raise ValueError(f"{name} must be a non-empty two-dimensional matrix")
    if not np.isfinite(matrix).all():
        raise ValueError(f"{name} must contain only finite values")
    return matrix


def _immutable(values: FloatArray) -> FloatArray:
    encoded = values.astype(np.float64, copy=False).tobytes()
    return np.frombuffer(encoded, dtype=np.float64)


@dataclass(frozen=True, slots=True)
class ScalingParameters:
    mean: FloatArray
    scale: FloatArray

    def __post_init__(self) -> None:
        mean = np.asarray(self.mean, dtype=np.float64)
        scale = np.asarray(self.scale, dtype=np.float64)
        if mean.ndim != 1 or scale.ndim != 1 or not mean.size:
            raise ValueError("mean and scale must be non-empty one-dimensional arrays")
        if mean.shape != scale.shape:
            raise ValueError("mean and scale must have equal dimensions")
        if not np.isfinite(mean).all() or not np.isfinite(scale).all():
            raise ValueError("mean and scale must be finite")
        if np.any(scale <= 0):
            raise ValueError("scale values must be positive")
        object.__setattr__(self, "mean", _immutable(mean))
        object.__setattr__(self, "scale", _immutable(scale))


def fit_scaler(training: npt.ArrayLike) -> ScalingParameters:
    matrix = _as_finite_matrix(training, name="training")
    mean = matrix.mean(axis=0)
    scale = matrix.std(axis=0)
    scale[scale == 0.0] = 1.0
    return ScalingParameters(mean, scale)


def transform_features(
    values: npt.ArrayLike, parameters: ScalingParameters
) -> FloatArray:
    if not isinstance(parameters, ScalingParameters):
        raise TypeError("parameters must be ScalingParameters")
    matrix = _as_finite_matrix(values, name="values")
    if matrix.shape[1] != parameters.mean.size:
        raise ValueError("values must have the fitted feature count")
    return (matrix - parameters.mean) / parameters.scale
