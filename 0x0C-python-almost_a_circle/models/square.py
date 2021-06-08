#!/usr/bin/python3
"""a class for a square
that inherits from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a square that inherits form the Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """the initialization of class square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retirng the value for size"""
        return self.height

    @size.setter
    def size(self, value):
        """setting the value of size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) > 0:
            for x in range(len(args)):
                if x == 0:
                    setattr(self, "id", args[0])
                if x == 1:
                    setattr(self, "height", args[1])
                if x == 2:
                    setattr(self, "x", args[2])
                if x == 3:
                    setattr(self, "y", args[3])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """return a string with to represetantion of the class square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
