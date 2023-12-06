#!/usr/bin/python3

"""Dictionary description with simple data structure"""


def class_to_json(obj):
    """Dictionary description of simple data structure
        of JSON serialization of an Obj
    """

    return obj.__dict__
