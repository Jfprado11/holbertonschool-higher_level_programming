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
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """gives the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ printing the string method of the instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
