"""Intensity normalisation."""

from __future__ import annotations

import numpy as np


def robust_normalize(image: np.ndarray, low: float = 1.0, high: float = 99.0) -> np.ndarray:
    """Clip to the ``[low, high]`` percentiles and rescale to [0, 1].

    A constant image maps to all zeros.
    """
    if not 0.0 <= low < high <= 100.0:
        raise ValueError("require 0 <= low < high <= 100")
    arr = np.asarray(image, dtype=float)
    if arr.size == 0:
        raise ValueError("image must be non-empty")
    lo, hi = np.percentile(arr, [low, high])
    if hi <= lo:
        return np.zeros_like(arr)
    return np.clip((arr - lo) / (hi - lo), 0.0, 1.0)
