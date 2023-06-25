import json


def get_web_url(file_path, key):
    with open(file_path, "r") as config_file:
        config_data = json.load(config_file)
    return config_data[key]
