import importlib

import pytest

SUBPACKAGES = ["models", "representations", "evaluation", "imaging", "utils"]


def test_version():
    import ibca_core

    assert ibca_core.__version__ == "0.1.0"


@pytest.mark.parametrize("name", SUBPACKAGES)
def test_subpackage_imports(name):
    assert importlib.import_module(f"ibca_core.{name}") is not None
