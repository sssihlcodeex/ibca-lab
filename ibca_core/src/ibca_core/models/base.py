"""Abstract model interface and a small name-based registry."""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, Type

import numpy as np

_REGISTRY: Dict[str, Type["BaseModel"]] = {}


class BaseModel(ABC):
    """Minimal interface every IBCA model should implement."""

    @abstractmethod
    def fit(self, x: np.ndarray, y: np.ndarray | None = None) -> "BaseModel":
        """Fit the model and return ``self``."""

    @abstractmethod
    def predict(self, x: np.ndarray) -> np.ndarray:
        """Return predictions for ``x``."""


def register_model(name: str) -> Callable[[Type[BaseModel]], Type[BaseModel]]:
    """Class decorator registering a model under ``name``."""

    def decorator(cls: Type[BaseModel]) -> Type[BaseModel]:
        if name in _REGISTRY:
            raise ValueError(f"model {name!r} is already registered")
        _REGISTRY[name] = cls
        return cls

    return decorator


def get_model(name: str, **kwargs: Any) -> BaseModel:
    try:
        cls = _REGISTRY[name]
    except KeyError:
        raise KeyError(f"unknown model {name!r}; available: {available_models()}") from None
    return cls(**kwargs)


def available_models() -> list[str]:
    return sorted(_REGISTRY)
