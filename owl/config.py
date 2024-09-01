import json


def load_config(filename: str):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
