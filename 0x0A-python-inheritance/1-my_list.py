#!/bin/usr/python3
""" a moudule for a class
that inherentce from the object reacriting a list
"""


class MyList(list):
    """A class that inherits from a list"""

    def print_sorted(self):
        """prints a sorted array"""
        print(sorted(self))
