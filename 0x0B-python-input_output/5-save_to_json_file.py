#!/usr/bin/python3

"""Writes an object to a text file using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Object to a text file, using a JSON representation

        Args:
            my_obj: The object to be serialized and saved to the file.
            filename (str): Path to the file.

        Return:
            None
    """

    with open(filename, mode="w", encoding="UTF-8") as file:
        obj_json = json.dumps(my_obj)
        file.write(obj_json)
