import json
import os

DB_FILE = "serial_store.json"


def load_database():

    if not os.path.exists(DB_FILE):
        return {}

    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_database(data):

    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)