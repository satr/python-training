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
make exercise EXERCISE=exercises/track01_core/exercise01_values_and_strings
```

Optional ecosystem libraries used by later data and AI extensions can be
installed with:

```bash
python -m pip install -e ".[data,ai]"
```

The core exercises intentionally use the standard library so the complete
training suite remains fast and portable.
