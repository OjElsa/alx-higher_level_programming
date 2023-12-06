#!/usr/bin/python3

"""Defines a Python data structure represented by a JSON string"""


import json


def from_json_string(my_str):
    """Returns data represented in JSON string"""
    return json.loads(my_str)
