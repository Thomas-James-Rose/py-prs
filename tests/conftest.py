import os
import pytest

import py_prs


@pytest.fixture(autouse=True)
def override_config_path(monkeypatch):
    test_config_path = f"{os.path.dirname(os.path.realpath(__file__))}/../.pyprs/config.json"
    os.makedirs(os.path.dirname(test_config_path), exist_ok=True)
    monkeypatch.setattr(py_prs.config, "config_path", test_config_path)
    open(test_config_path, "w+")
