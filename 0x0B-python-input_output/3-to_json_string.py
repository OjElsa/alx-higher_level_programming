#!/usr/bin/python3

"""Module for json operations on files"""


import json


def to_json_string(my_obj):
    """JSON representation of the object"""
    return json.dumps(my_obj)
