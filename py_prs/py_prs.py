import argparse
from . import reviews
from . import config

parser = argparse.ArgumentParser(description="")

subparsers = parser.add_subparsers(help="")

parser_set = subparsers.add_parser("set", help="Set the GitHub User ID or access token")
parser_set.add_argument("--user", type=str, nargs=1, help="GitHub User ID")
parser_set.add_argument("--token", type=str, nargs=1, help="GitHub Access Token")
parser_set.set_defaults(func=config.set)

parser_list = subparsers.add_parser("list", help="List PRs that need reviewing")
parser_list.set_defaults(func=reviews.get_review_requests)

def parse_command():
  args = parser.parse_args()
  args.func(args)