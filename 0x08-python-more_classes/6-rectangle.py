#!/usr/bin/python3
"""a class to defing a rectangle"""


class Rectangle:
    """a class have a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialization of the atributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """returs the representation of the rectangle with '#'"""
        cont = ""
        if self.__height == 0 or self.__width == 0:
            return cont
        for i in range(self.__height):
            for x in range(self.__width):
                cont = cont + "#"
            if i < self.__height - 1:
                cont = cont + "\n"
        return cont

    def __repr__(self):
        """a string representation of the rectangle to be able to
        recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """delete a instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """method to get the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method the get the area of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
