import json
import requests
from string import Template
from . import config
from . import console_colours

query_template = Template("""
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
""")


def get_review_requests(args):
    with open(config.config_path, "r") as config_file:
        user_config = json.load(config_file)

    if "user" not in user_config:
        print(
            f"{console_colours.WARNING}🚨 A user has not been configured. Please use 'pyprs set --user <GITHUB_USER_ID>' to configure one.{console_colours.ENDC}"
        )
        return

    if "token" not in user_config:
        print(
            f"{console_colours.WARNING}🚨 An access token has not been configured. Please use 'pyprs set --token <GITHUB_ACCESS_TOKEN>' to configure one.{console_colours.ENDC}"
        )
        return

    query = query_template.substitute(user_id=user_config["user"][0])

    auth_header = Template("bearer $access_token").substitute(
        access_token=user_config["token"][0])
    response = requests.post(
        "https://api.github.com/graphql",
        json={"query": query},
        headers={"Authorization": auth_header},
    )

    response_json = json.loads(response.text)
    nodes = response_json["data"]["search"]["edges"]

    print(f"{console_colours.HEADER}🐍 PyPrs 🐍{console_colours.ENDC}")

    if (len(nodes) > 0):
        print(
            f"{console_colours.OKBLUE}Grab yourself a brew and review these PRs... 🫖{console_colours.ENDC}"
        )
        for node in nodes:
            print(node["node"]["url"])
    else:
        print(
            f"{console_colours.OKBLUE}Nothing to see here! 👀{console_colours.ENDC}"
        )
