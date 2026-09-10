# Installation

## Requirements

- Python 3.11 or newer
- `make` (optional; all commands can be run directly)
- Git

## Environment

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev,data,ai,pytorch]"
```

In Windows PowerShell, create and activate the environment with:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev,data,ai,pytorch]"
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

Make targets use `.venv/bin/python` on macOS/Linux or
`.venv/Scripts/python.exe` on Windows when that interpreter exists. Otherwise
they fall back to `python3` on macOS/Linux or `python` on Windows. Set
`PYTHON` to use a different interpreter explicitly.

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
