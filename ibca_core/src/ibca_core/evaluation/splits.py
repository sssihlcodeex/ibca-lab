"""Leakage-resistant splitting.

Samples that share a group (for example a plate, scaffold or subject) are never
placed on both sides of a split.
"""

from __future__ import annotations

from typing import Sequence

import numpy as np


def group_holdout_split(
    groups: Sequence, test_fraction: float = 0.2, seed: int = 0
) -> tuple[np.ndarray, np.ndarray]:
    """Return ``(train_idx, test_idx)`` with whole groups held out.

    At least one group lands in each side, so at least two distinct groups are required.
    """
    if not 0.0 < test_fraction < 1.0:
        raise ValueError("test_fraction must lie strictly between 0 and 1")
    arr = np.asarray(groups)
    unique = np.unique(arr)
    if unique.size < 2:
        raise ValueError("need at least two distinct groups for a group-held-out split")
    rng = np.random.default_rng(seed)
    shuffled = rng.permutation(unique)
    n_test = min(max(1, round(test_fraction * unique.size)), unique.size - 1)
    test_groups = shuffled[:n_test]
    test_mask = np.isin(arr, test_groups)
    idx = np.arange(arr.size)
    train_idx, test_idx = idx[~test_mask], idx[test_mask]
    assert_no_group_overlap(arr[train_idx], arr[test_idx])
    return train_idx, test_idx


def assert_no_group_overlap(train_groups: Sequence, test_groups: Sequence) -> None:
    """Raise ``ValueError`` if any group appears in both partitions."""
    shared = set(np.asarray(train_groups).tolist()) & set(np.asarray(test_groups).tolist())
    if shared:
        raise ValueError(f"group leakage: {sorted(shared, key=str)} appear in train and test")
