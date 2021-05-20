#!/usr/bin/python3
"""a class to defing a rectangle"""


class Rectangle:
    """a class have a rectangle"""

    def __init__(self, width=0, height=0):
        """initialization of the atributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriving width as a private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """given to the atribute a value if
        the value is not an int error rise an error
        or if the value a negative int raise error"""
        if isinstance(value, int):
            self.__width = value
        else:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """retriving height as a private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """given to the atribute a value if
        the value is not an int error rise an error
        or if the value a negative int raise error"""
        if isinstance(value, int):
            self.__height = value
        else:
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
