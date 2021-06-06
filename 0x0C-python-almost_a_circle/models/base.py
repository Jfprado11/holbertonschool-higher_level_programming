#!/usr/bin/python3
"""A module with a
class for the base of the rest of clases
"""


class Base():
    """a class base for the rest"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the contructor for the class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects