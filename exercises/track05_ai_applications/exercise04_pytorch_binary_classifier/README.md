# PyTorch binary classifier

## Theory

A linear binary classifier maps each feature row to one logit. Combining
`BCEWithLogitsLoss` with stochastic gradient descent provides a small training
loop while avoiding the numerical instability of applying a sigmoid before
the loss. Reproducible examples should make device and initialization choices
explicit.

## Learn before coding

Convert arrays with `torch.tensor(values, dtype=torch.float32)` and keep one
row per example. A linear model produces logits; `torch.sigmoid(logits)` maps
them to probabilities between zero and one. Binary cross-entropy with logits
combines these steps safely. A training loop is: validate shapes and labels,
create CPU tensors and parameters, compute loss, call `optimizer.zero_grad()`,
`loss.backward()`, and `optimizer.step()`, then record requested values. Set a
deterministic seed before initialization, avoid changing caller arrays, and
check that epochs and learning rate are valid.

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
