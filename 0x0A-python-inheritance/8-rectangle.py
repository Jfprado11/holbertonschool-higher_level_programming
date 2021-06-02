#!/usr/bin/python3
""" a class that will
inherented from a class basicGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """inherits from a class
    with basic calculations
    """

    def __init__(self, width, height):
        """initiation of the class
        containing the super class to bring up the methods
        from the paretn class
        """
        self.__width = width
        self.__height = height
        super().__init__()
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
