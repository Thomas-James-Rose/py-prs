import argparse
import io
import os
import requests
import sys

import py_prs.console_colours
import py_prs

test_config_path = f"{os.path.dirname(os.path.realpath(__file__))}/.pyprs/config.json"
os.makedirs(os.path.dirname(test_config_path), exist_ok=True)


class MockResponse:
    def __init__(self, text):
        self.text = text


mock_gh_response_text = """{
  "data": {
    "search": {
      "issueCount": 1,
      "pageInfo": {
        "endCursor": "Y3Vyc29yOjE=",
        "startCursor": "Y3Vyc29yOjE="
      },
      "edges": [
        {
          "node": {
            "repository": {
              "nameWithOwner": "JohnDoe/foo-bar"
            },
            "number": 7,
            "url": "https://github.com/JohnDoe/foo-bar/pull/7"
          }
        }
      ]
    }
  }
}"""


def run_and_get_console_output(func):
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    func()
    sys.stdout = sys.__stdout__
    return capturedOutput.getvalue()


def test_get_review_requests(monkeypatch):
    mock_gh_response = MockResponse(mock_gh_response_text)

    monkeypatch.setattr(py_prs.config, "config_path", test_config_path)
    monkeypatch.setattr(requests, "post",
                        lambda url, json, headers: mock_gh_response)

    user = "JohnDoe"
    token = "ghp_qwertyyuiopasdfghjklzxcvbnm"

    py_prs.config.set(argparse.Namespace(user=[user], token=token))
    output = run_and_get_console_output(
        lambda: py_prs.reviews.get_review_requests(argparse.Namespace()))

    expected_output = (
        f"{py_prs.console_colours.HEADER}🐍 PyPrs 🐍{py_prs.console_colours.ENDC}\n"
        f"{py_prs.console_colours.OKBLUE}Grab yourself a brew and review these PRs... 🫖{py_prs.console_colours.ENDC}\n"
        f"https://github.com/JohnDoe/foo-bar/pull/7\n")

    assert output == expected_output
