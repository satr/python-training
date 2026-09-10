# Installation

## Requirements

- Python 3.11 or newer
- `make` (optional; all commands can be run directly)
- Git

## Environment

```bash
python3 -m venv .venv
source .venv/bin/activate       # Windows PowerShell: .venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Run the fast local checks:

```bash
make check
```

Run one exercise:

```bash
make 01_core_01_values_and_strings
```

Run `make help` to see the dedicated target for every exercise.

Optional ecosystem libraries used by the data and lightweight AI exercises
can be installed with:

```bash
python -m pip install -e ".[data,ai]"
```

PyTorch is separate so the `ai` extra stays lightweight:

```bash
python -m pip install -e ".[ai,pytorch]"
```

Install all exercise and validation dependencies with
`python -m pip install -e ".[dev,data,ai,pytorch]"`. Core exercises
intentionally use the standard library and remain fast and portable.
