import argparse
import io
import os
import pytest
import sys
from string import Template

import py_prs

test_config_path = f"{os.path.dirname(os.path.realpath(__file__))}/.pyprs/config.json"

os.makedirs(os.path.dirname(test_config_path), exist_ok=True)


@pytest.fixture(autouse=True)
def run_around_tests():
    open(test_config_path, "w+")


def run_and_get_console_output(func):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    func()
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()


def test_set_user(monkeypatch):
    monkeypatch.setattr(py_prs.config, "config_path", test_config_path)

    user = "JohnDoe"

    output = run_and_get_console_output(
        lambda: py_prs.config.set(argparse.Namespace(user=[user], token=None)))

    assert output == Template("{'user': ['$user_id']}\n").substitute(
        user_id=user)


def test_set_access_token(monkeypatch):
    monkeypatch.setattr(py_prs.config, "config_path", test_config_path)

    token = "ghp_qwertyyuiopasdfghjklzxcvbnm"

    output = run_and_get_console_output(lambda: py_prs.config.set(
        argparse.Namespace(user=None, token=[token])))

    assert output == Template("{'token': ['$access_token']}\n").substitute(
        access_token=token)
