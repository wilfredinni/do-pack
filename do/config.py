import os
import json


path_config = os.path.join(
    os.path.dirname(__file__), 'config.json')


def load_json():
    with open(path_config, 'r') as f:
        return json.load(f)


def write_json():
    pass


if __name__ == '__main__':
    print(load_json().values())
