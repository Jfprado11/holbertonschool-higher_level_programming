#!/usr/bin/python3
"""learning how to use class and methods
for this excersize we will create a class
squere to know the squre root of some functions"""


class Square:
    """defines a square by"""
    def __init__(self, size=0, position=(0, 0)):
        """init the class
        args:
            param 1(size): the size of squere"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """retrinving the attribute position as private"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of a tuple"""
        if len(value) < 2:
            raise TypeError("""position must be a tuple\
 of 2 positive integers""")
        for i in range(len(value)):
            if isinstance(value[i], int) is False:
                raise TypeError("""position must be a tuple\
 of 2 positive integers""")
        self.__position = value

    def area(self):
        """find the squere area"""
        return self.__size ** 2

    def my_print(self):
        """prints a squere with the '#'"""
        if self.__size == 0:
            print()
        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()
