#!/usr/bin/python3
"""A module witch it hold a
class base geometry
"""


class BaseGeometry:
    """A class with a method
    that raises an Error
    """

    def area(self):
        """ A method that
        raises an error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """" check if the passes value
        is a integer
        if not raises an error
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
