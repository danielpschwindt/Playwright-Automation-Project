import json

def load_config():
    with open("config/config.json") as file:
        return json.load(file)
    