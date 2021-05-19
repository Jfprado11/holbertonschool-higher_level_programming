#!/usr/bin/python3
"""learning how to use class and methods
for this excersize we will create a class
squere to know the squre root of some functions"""


class Square:
    """defines a square by"""
    def __init__(self, size=0):
        """init the class
        args:
            param 1(size): the size of squere"""
        self.__size = size

    @property
    def size(self):
        """retriving the atributte size as private"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value"""
        if isinstance(value, int) is True:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """find the squere area"""
        return self.__size ** 2
