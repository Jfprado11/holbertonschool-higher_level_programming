#!/usr/bin/python3
"""
chekck if a object is a instance of
a class or if it is a intance inherited
"""


def is_kind_of_class(obj, a_class):
    """check if a intance come from a
    specific object"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
