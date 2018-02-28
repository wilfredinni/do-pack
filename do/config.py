import os
import json


path_config = os.path.join(
    os.path.dirname(__file__), 'config.json')


def load_json():
    with open(path_config, 'r') as f:
        return json.load(f)


def write_json(author, mail):
    loaded_config = load_json()
    loaded_config['default_author'] = author
    loaded_config['default_mail'] = mail

    with open(path_config, 'w') as f:
        json.dump(loaded_config, f)


def show_common(field):
    loaded_config = load_json()
    return loaded_config[field]


if __name__ == '__main__':
    a = show_common('default_author')
    print(a)
