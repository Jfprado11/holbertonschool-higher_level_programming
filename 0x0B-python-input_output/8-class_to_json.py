#!/usr/bin/python3
"""
a function that will return
a diccionary of the atributes of a class
in a json string represetantion
"""


def class_to_json(obj):
    """function
    that returs a vars
    to a return a diccionary of an object
    """
    return vars(obj)
