#!/usr/bin/python3

"""check if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """check if an object is an instance of a class if inherited or not
    
    Args:
        obj(object) - is an object to be checked
        a_class(class) : class to check the object

    Returns:
        True if `obj` is inherited from `a_class`, False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
