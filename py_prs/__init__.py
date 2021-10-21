from . import py_prs
from . import reviews
from . import config
import os

os.makedirs(os.path.dirname(config.config_path), exist_ok=True)

with open(config.config_path, 'a') as config_file:
    if config_file.tell() == 0:
        config_file.write("{}")

parse = py_prs.parse_command
