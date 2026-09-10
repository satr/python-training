# NumPy feature scaling

## Theory

Feature scaling estimates statistics from training data and reuses those
statistics for validation, test, and production inputs. Re-fitting on later
data leaks information and makes evaluation unreliable. Constant columns need
a safe scale so transformation never divides by zero.

## Learn before coding

Convert input with `np.asarray(values, dtype=np.float64)` and use `axis=0`
for one statistic per feature column. Standard scaling is
`(values - mean) / scale`; `np.mean([[1, 3], [5, 7]], axis=0)` computes
column means.

- Keep fitting and transformation separate:
  - Fit parameters from training rows only.
  - Replace a zero population scale according to the contract.
  - Apply saved parameters to later rows without re-fitting.
- Validate two-dimensional, finite, compatible arrays, and copy inputs when a
  transformation must not mutate caller data.

## Task

- Implement `ScalingParameters`, `fit_scaler`, and `transform_features`.
- Fit parameters with these rules:
  - Use column-wise means and population standard deviations from a non-empty,
    two-dimensional finite numeric matrix.
  - Keep parameters immutable.
  - Use a scale of one for constant columns.
- During transformation, validate feature counts, return new arrays, and never
  change or re-fit from the input matrix.

## Run

```bash
make 05_ai_applications_03_numpy_feature_scaling
```

Install the `ai` extra first.

## Further practice

Add an inverse transform and compare standard scaling with robust median and
interquartile-range scaling.
