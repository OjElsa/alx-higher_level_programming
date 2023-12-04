#!/usr/bin/python3

"""Returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns an attributes and methods of an object

        Args:
            obj (object): an object

        """
    return dir(obj)
