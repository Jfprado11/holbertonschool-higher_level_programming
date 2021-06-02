#!/usr/bin/python3
"""A module witch it hold a
class base geometry with two methods
withc raises errors
"""


class BaseGeometry:
    """A class with a method
    that raises an Error
    """

    def area(self):
        """ A method that
        raises an error the area is not implemeted
        yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """" check if the passes value
        is a integer
        if not raises an typeError if not value is int
        if the value is less or equal than 0 raises
        a valueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
