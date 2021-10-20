import argparse
import py_prs

parser = argparse.ArgumentParser(description='')
parser.add_argument('command', metavar='cmd', type=str, help='')

def parse_command():
  args = parser.parse_args()
  
  commands = {
    "list": py_prs.reviews.get_review_requests,
    "set": py_prs.config.set
  }

  commands[args.command]()