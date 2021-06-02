#!/usr/bin/python3
"""A method that holds a class
witch it inherates from the class
rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class witch holds
    an inheratence of rectangle
    """

    def __init__(self, size):
        """ initiation of the class
        containing the super class to bring up the methods
        from the paretn class
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        """gives the area of a square"""
        return self.__size * self.__size
