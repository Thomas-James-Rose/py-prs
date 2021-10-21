import json
import requests
from string import Template
from . import config


def get_review_requests(args):
    with open(config.config_path, "r") as config_file:
        user_config = json.load(config_file)

    if "user" not in user_config:
        print(
            "A user has not been configured. Please use 'pyprs set --user <GITHUB_USER_ID>' to configure one."
        )
        return

    if "token" not in user_config:
        print(
            "An access token has not been configured. Please use 'pyprs set --token <GITHUB_ACCESS_TOKEN>' to configure one."
        )
        return

    query = Template("""
    {
      search(query: "type:pr state:open review-requested:$user_id", type: ISSUE, first: 100) {
        issueCount
        pageInfo {
          endCursor
          startCursor
        }
        edges {
          node {
            ... on PullRequest {
              repository {
                nameWithOwner
              }
              number
              url
            }
          }
        }
      }
    }
    """).substitute(user_id=user_config["user"][0])

    auth_header = Template("bearer $access_token").substitute(
        access_token=user_config["token"][0])
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query},
        headers={"Authorization": auth_header},
    )

    response_json = json.loads(response.text)
    nodes = response_json["data"]["search"]["edges"]

    for node in nodes:
        print(node["node"]["url"])
