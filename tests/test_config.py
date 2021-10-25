import argparse
import io
import os
import pytest
import sys
from string import Template

import py_prs


def run_and_get_console_output(func):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    func()
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()


def test_set_user():
    user = "JohnDoe"

    output = run_and_get_console_output(
        lambda: py_prs.config.set(argparse.Namespace(user=[user], token=None)))

    assert output == Template("{'user': ['$user_id']}\n").substitute(
        user_id=user)


def test_set_access_token():
    token = "ghp_qwertyyuiopasdfghjklzxcvbnm"

    output = run_and_get_console_output(lambda: py_prs.config.set(
        argparse.Namespace(user=None, token=[token])))

    assert output == Template("{'token': ['$access_token']}\n").substitute(
        access_token=token)
