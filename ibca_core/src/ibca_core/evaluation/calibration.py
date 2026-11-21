"""Calibration metrics."""

from __future__ import annotations

import numpy as np


def expected_calibration_error(
    confidences: np.ndarray, correct: np.ndarray, n_bins: int = 15
) -> float:
    """Expected calibration error with equal-width confidence bins.

    Args:
        confidences: Predicted confidence of the chosen class, in [0, 1].
        correct: Boolean/0-1 array, 1 where the prediction was right.
        n_bins: Number of equal-width bins.
    """
    conf = np.asarray(confidences, dtype=float)
    corr = np.asarray(correct, dtype=float)
    if conf.shape != corr.shape or conf.ndim != 1:
        raise ValueError("confidences and correct must be 1-D arrays of equal length")
    if conf.size == 0:
        raise ValueError("inputs must be non-empty")
    if conf.min() < 0.0 or conf.max() > 1.0:
        raise ValueError("confidences must lie in [0, 1]")
    if n_bins < 1:
        raise ValueError("n_bins must be >= 1")
    edges = np.linspace(0.0, 1.0, n_bins + 1)
    bin_ids = np.clip(np.digitize(conf, edges[1:-1], right=True), 0, n_bins - 1)
    ece = 0.0
    for b in range(n_bins):
        mask = bin_ids == b
        if mask.any():
            ece += mask.mean() * abs(corr[mask].mean() - conf[mask].mean())
    return float(ece)
