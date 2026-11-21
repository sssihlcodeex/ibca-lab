"""Abstract interface for representation learners."""

from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class BaseRepresentation(ABC):
    """Learns a mapping from raw observations to a representation space."""

    @abstractmethod
    def fit(self, x: np.ndarray) -> "BaseRepresentation":
        """Fit on observations ``x`` and return ``self``."""

    @abstractmethod
    def transform(self, x: np.ndarray) -> np.ndarray:
        """Map observations ``x`` to representations."""

    def fit_transform(self, x: np.ndarray) -> np.ndarray:
        return self.fit(x).transform(x)
