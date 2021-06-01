#!/usr/bin/python3
"""a function that returns
True if the object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    if type(obj) is a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
