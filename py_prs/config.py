import json
import os

config_path = f"{os.path.expanduser('~')}/.pyprs/config.json"


def set(args):
    with open(config_path, "r") as config_file:
        try:
            config = json.load(config_file)
        except:
            config = {}

    with open(config_path, "w+") as config_file:
        if args.user != None:
            config["user"] = args.user

        if args.token != None:
            config["token"] = args.token

        config_file.write(json.dumps(config))

    with open(config_path, "r") as config_file:
        config = json.load(config_file)
        print(config)
