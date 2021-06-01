#!/usr/bin/python3
"""a module taht has a function
witch return the methods of an objecta can hold"""


def lookup(obj):
    """a function that recives an object
    and return a list with its methods that the object can
    hold"""
    return dir(obj)
