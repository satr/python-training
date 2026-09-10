# NumPy feature scaling

## Theory

Feature scaling estimates statistics from training data and reuses those
statistics for validation, test, and production inputs. Re-fitting on later
data leaks information and makes evaluation unreliable. Constant columns need
a safe scale so transformation never divides by zero.

## Task

Implement `ScalingParameters`, `fit_scaler`, and `transform_features`. Fit
column-wise means and population standard deviations from a non-empty,
two-dimensional finite numeric matrix. Keep parameters immutable, use a scale
of one for constant columns, validate feature counts, return new arrays, and
never change or re-fit from a matrix passed for transformation.

## Run

```bash
make 05_ai_applications_03_numpy_feature_scaling
```

Install the `ai` extra first.

## Further practice

Add an inverse transform and compare standard scaling with robust median and
interquartile-range scaling.
