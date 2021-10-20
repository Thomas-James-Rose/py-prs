from . import py_prs
from . import reviews
from . import config
import os

config_path = f"{os.path.expanduser('~')}/.pyprs/config.json"

os.makedirs(os.path.dirname(config_path), exist_ok=True)
open(config_path, "w")

parse = py_prs.parse_command
