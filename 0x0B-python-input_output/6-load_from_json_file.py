#!/usr/bin/python3

"""Creates an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file.

        Args:
            filename (str): Path to the JSON file.

        Return:
            object: Python object created from the JSON file
    """

    with open(filename, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data
