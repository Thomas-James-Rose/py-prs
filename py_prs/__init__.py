from . import py_prs
from . import reviews
from . import config
import os

os.makedirs(os.path.dirname(config.config_path), exist_ok=True)
open(config.config_path, "w")

parse = py_prs.parse_command
