# PyTorch binary classifier

## Theory

A linear binary classifier maps each feature row to one logit. Combining
`BCEWithLogitsLoss` with stochastic gradient descent provides a small training
loop while avoiding the numerical instability of applying a sigmoid before
the loss. Reproducible examples should make device and initialization choices
explicit.

## Learn before coding

Convert arrays while keeping one row per example:

```python
torch.tensor(values, dtype=torch.float32)
```

A linear model produces logits. This operation maps them to probabilities
between zero and one:

```python
torch.sigmoid(logits)
```

Binary cross-entropy with logits combines these steps safely.

- Follow the training loop in order:
  - Validate shapes, labels, epochs, and learning rate.
  - Set a deterministic seed before initialization.
  - Create CPU tensors and parameters.
  - Compute loss.
  - Run the optimizer sequence in order:

    ```python
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    ```
  - Record the requested values.
- Do not change caller arrays.

## Task

- Implement `train_binary_classifier`.
- Validate inputs:
  - Require finite two-dimensional NumPy features.
  - Require a matching one-dimensional binary label vector.
  - Require positive epochs and learning rate.
- Train a zero-initialized linear classifier on CPU with PyTorch tensors,
  `BCEWithLogitsLoss`, and `SGD`.
- Return an immutable `TrainingResult` containing:
  - Initial loss.
  - Final loss.
  - One probability per row.
- Do not mutate the NumPy inputs.

## Run

```bash
make 05_ai_applications_04_pytorch_binary_classifier
```

Install the `ai` and `pytorch` extras first.

## Further practice

Add a validation split and report threshold-independent metrics without
changing the training data statistics.
