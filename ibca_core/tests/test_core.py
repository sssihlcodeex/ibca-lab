import numpy as np
import pytest

from ibca_core.evaluation import (
    assert_no_group_overlap,
    expected_calibration_error,
    group_holdout_split,
)
from ibca_core.imaging import robust_normalize
from ibca_core.models import available_models, get_model, register_model, BaseModel
from ibca_core.utils import set_seed


def test_group_split_has_no_leakage():
    groups = np.repeat(np.arange(10), 5)
    tr, te = group_holdout_split(groups, test_fraction=0.3, seed=1)
    assert set(groups[tr]).isdisjoint(groups[te])
    assert len(tr) + len(te) == len(groups)


def test_group_split_needs_two_groups():
    with pytest.raises(ValueError):
        group_holdout_split([1, 1, 1])


def test_overlap_detected():
    with pytest.raises(ValueError):
        assert_no_group_overlap([1, 2], [2, 3])


def test_ece_perfect_and_bad():
    assert expected_calibration_error(np.array([1.0, 1.0]), np.array([1, 1])) == 0.0
    assert expected_calibration_error(np.array([1.0, 1.0]), np.array([0, 0])) == pytest.approx(1.0)


def test_normalize_range_and_constant():
    out = robust_normalize(np.arange(100.0))
    assert out.min() == 0.0 and out.max() == 1.0
    assert not robust_normalize(np.ones((4, 4))).any()


def test_set_seed_reproducible():
    set_seed(5)
    a = np.random.rand(3)
    set_seed(5)
    assert np.array_equal(a, np.random.rand(3))


def test_registry():
    @register_model("test-dummy")
    class Dummy(BaseModel):
        def fit(self, x, y=None):
            return self

        def predict(self, x):
            return x

    assert "test-dummy" in available_models()
    assert isinstance(get_model("test-dummy"), Dummy)
    with pytest.raises(KeyError):
        get_model("missing")
