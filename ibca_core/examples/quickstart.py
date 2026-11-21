"""Minimal tour of ibca_core. Uses synthetic data only."""

import numpy as np

from ibca_core import ExperimentConfig
from ibca_core.evaluation import expected_calibration_error, group_holdout_split
from ibca_core.imaging import robust_normalize
from ibca_core.utils import set_seed

cfg = ExperimentConfig(name="quickstart", track="cellular-microscopy", seed=42)
set_seed(cfg.seed)

# Synthetic "plates": whole plates are held out, never split across partitions.
plates = np.repeat(np.arange(8), 12)
train_idx, test_idx = group_holdout_split(plates, cfg.test_fraction, cfg.seed)
print(f"train={len(train_idx)} test={len(test_idx)} held-out plates={sorted(set(plates[test_idx].tolist()))}")

img = robust_normalize(np.random.default_rng(cfg.seed).normal(size=(64, 64)))
print(f"normalised image range: [{img.min():.2f}, {img.max():.2f}]")

conf = np.random.default_rng(cfg.seed).uniform(0.5, 1.0, size=200)
correct = np.random.default_rng(cfg.seed + 1).uniform(size=200) < conf
print(f"ECE on synthetic predictions: {expected_calibration_error(conf, correct):.3f}")
