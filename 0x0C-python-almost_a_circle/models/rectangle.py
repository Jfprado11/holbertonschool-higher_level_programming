#!/usr/bin/python3
"""a module that holds a class
rectangle
"""
from models.base import Base


class Rectangle(Base):
    """a class that inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the constructor of the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retriving width as a private instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """setting the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retriving height as a private instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """setting the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """retriving x as a private instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """setting the value of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """retriving y as a private instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """setting the value of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """gets the area of a rectangle"""
        return (self.__height) * (self.__width)

    def display(self):
        """mehtod for display the rectangle"""
        for y in range(self.__y):
            print()

        for x in range(self.__height):
            for l in range(self.__x):
                print(" ", end="")
            for i in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """gives the string format of an class Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            for x in range(len(args)):
                if x == 0:
                    setattr(self, "id", args[0])
                if x == 1:
                    setattr(self, "width", args[1])
                if x == 2:
                    setattr(self, "height", args[2])
                if x == 3:
                    setattr(self, "x", args[3])
                if x == 4:
                    setattr(self, "y", args[4])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        dic = {}
        for x in self.__dict__.keys():
            if x == "_Rectangle__x":
                dic["x"] = self.__dict__[x]
            if x == "_Rectangle__y":
                dic["y"] = self.__dict__[x]
            if x == "id":
                dic["id"] = self.__dict__[x]
            if x == "_Rectangle__height":
                dic["height"] = self.__dict__[x]
            if x == "_Rectangle__width":
                dic["width"] = self.__dict__[x]
        return dic
