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
        """ initializate the class
        with its atributes
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)
