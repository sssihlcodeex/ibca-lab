import pytest

from ibca_core import TRACKS, ExperimentConfig


def test_tracks_are_the_three_defined():
    assert TRACKS == ("cellular-microscopy", "clinical-ai", "quantitative-bioimaging")


def test_valid_config_roundtrip():
    cfg = ExperimentConfig(name="demo", track="clinical-ai", seed=3)
    assert ExperimentConfig.from_dict(cfg.to_dict()) == cfg


@pytest.mark.parametrize(
    "kwargs",
    [
        {"name": "", "track": "clinical-ai"},
        {"name": "x", "track": "unknown-track"},
        {"name": "x", "track": "clinical-ai", "split_strategy": "bogus"},
        {"name": "x", "track": "clinical-ai", "test_fraction": 1.0},
        {"name": "x", "track": "clinical-ai", "seed": -1},
    ],
)
def test_invalid_config_rejected(kwargs):
    with pytest.raises(ValueError):
        ExperimentConfig(**kwargs)


def test_unknown_key_rejected():
    with pytest.raises(ValueError):
        ExperimentConfig.from_dict({"name": "x", "track": "clinical-ai", "oops": 1})
