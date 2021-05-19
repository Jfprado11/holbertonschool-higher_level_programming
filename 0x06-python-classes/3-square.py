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
        if isinstance(size, int) is True:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """find the squere area"""
        return self.__size ** 2
