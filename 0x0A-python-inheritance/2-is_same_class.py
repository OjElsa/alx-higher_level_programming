#!/usr/bin/python3

"""Defines check class function"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class
     Args:
        obj(object): An Object
        a_class (class): A class

    Returns:
        True of object is exact false if ortherwise
        """

    if type(obj) is a_class:
        return True
    else:
        return False
