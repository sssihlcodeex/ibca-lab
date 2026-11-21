"""Experiment configuration validated against the three IBCA Lab research tracks."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Mapping

TRACKS: tuple[str, ...] = (
    "cellular-microscopy",
    "clinical-ai",
    "quantitative-bioimaging",
)

SPLIT_STRATEGIES: tuple[str, ...] = ("group-holdout", "random")


@dataclass(frozen=True)
class ExperimentConfig:
    """Minimal, explicit description of an experiment run.

    Attributes:
        name: Short experiment identifier.
        track: One of :data:`TRACKS`.
        seed: Random seed recorded for reproducibility.
        split_strategy: ``"group-holdout"`` (leakage-resistant default) or ``"random"``.
        test_fraction: Fraction of groups/samples held out for testing, in (0, 1).
        output_dir: Directory for run artefacts (never commit its contents).
    """

    name: str
    track: str
    seed: int = 0
    split_strategy: str = "group-holdout"
    test_fraction: float = 0.2
    output_dir: str = "runs"

    def __post_init__(self) -> None:
        if not self.name or not self.name.strip():
            raise ValueError("name must be a non-empty string")
        if self.track not in TRACKS:
            raise ValueError(f"track must be one of {TRACKS}, got {self.track!r}")
        if self.split_strategy not in SPLIT_STRATEGIES:
            raise ValueError(
                f"split_strategy must be one of {SPLIT_STRATEGIES}, got {self.split_strategy!r}"
            )
        if not 0.0 < self.test_fraction < 1.0:
            raise ValueError("test_fraction must lie strictly between 0 and 1")
        if self.seed < 0:
            raise ValueError("seed must be non-negative")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "ExperimentConfig":
        known = set(cls.__dataclass_fields__)
        unknown = set(data) - known
        if unknown:
            raise ValueError(f"unknown config keys: {sorted(unknown)}")
        return cls(**data)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
