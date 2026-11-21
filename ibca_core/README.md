# ibca_core

Research library of **IBCA Lab — Identifiable Bio-Imaging & Clinical AI Lab**.

> Status: pre-alpha foundation. The package currently provides configuration,
> reproducibility helpers, leakage-aware split utilities, a calibration metric,
> an intensity-normalisation helper, and abstract interfaces for models and
> representations. It does **not** contain trained models, benchmarks, or
> clinically validated components.

## Install

```bash
cd ibca_core
python -m venv .venv && source .venv/bin/activate
pip install -e .          # core (NumPy only)
pip install -e ".[dev]"   # adds pytest
pytest
```

PyTorch is an optional extra (`pip install -e ".[torch]"`); nothing in the
core import path requires it.

## Layout

| Subpackage | Purpose | Current contents |
|---|---|---|
| `config` | Experiment configuration | `ExperimentConfig`, validated against the three research tracks |
| `models` | Model registry | Registry + `BaseModel` interface |
| `representations` | Representation learning | `BaseRepresentation` interface |
| `evaluation` | Validation | Group-held-out splits, overlap check, expected calibration error |
| `imaging` | Image utilities | Percentile intensity normalisation |
| `utils` | Reproducibility | `set_seed` |

## Quickstart

```bash
python examples/quickstart.py
```

Licensed under MIT. See `LICENSE`.
