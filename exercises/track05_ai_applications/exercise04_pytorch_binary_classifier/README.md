# PyTorch binary classifier

## Theory

A linear binary classifier maps each feature row to one logit. Combining
`BCEWithLogitsLoss` with stochastic gradient descent provides a small training
loop while avoiding the numerical instability of applying a sigmoid before
the loss. Reproducible examples should make device and initialization choices
explicit.

## Task

Implement `train_binary_classifier`. Validate finite two-dimensional NumPy
features, a matching one-dimensional binary label vector, and positive epochs
and learning rate. Train a zero-initialized linear classifier on CPU with
PyTorch tensors, `BCEWithLogitsLoss`, and `SGD`. Return an immutable
`TrainingResult` containing initial loss, final loss, and one probability per
row. Do not mutate the NumPy inputs.

## Run

```bash
make 05_ai_applications_04_pytorch_binary_classifier
```

Install the `ai` and `pytorch` extras first.

## Further practice

Add a validation split and report threshold-independent metrics without
changing the training data statistics.
