#!/usr/bin/python3

"""Defines a check class function"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance or inherited instance of a_class
    Args:
        obj (object): An object
        a_class (type): a class to check obj

    Returns:
        True if obj is an instance of a_class false if not
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
