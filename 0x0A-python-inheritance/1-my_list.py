#!/usr/bin/python3
""" a moudule for a class
that inherentce from the object reacreating a list
"""


class MyList(list):
    """A class that inherits from a list"""

    def __init__(self):
        """initialization of the class"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted array"""
        print(sorted(self))
