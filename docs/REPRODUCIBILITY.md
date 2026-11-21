# Reproducibility

Every experiment should record:

- Dataset provenance, version and licence
- Preprocessing steps and split construction
- Model configuration (`ibca_core.ExperimentConfig.to_dict()`)
- Random seeds (`ibca_core.utils.set_seed`)
- Software versions (pin or export the environment)
- Training procedure and evaluation metrics
- Known limitations

Set up the environment:

```bash
cd ibca_core
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Do not commit run outputs (`runs/`), checkpoints, caches or datasets.
