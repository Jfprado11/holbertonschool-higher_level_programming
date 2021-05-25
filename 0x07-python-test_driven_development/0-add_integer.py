#!/usr/bin/python3
"""A function that add two integer
if is a float: convert the float into a int
if is a different value from int or float: raise a error value
return the add of two integers
"""


def add_integer(a, b=98):
    """return the addintion of a and b
    if one of arguments if different from a int or float it raise a TypeError
    if one of the arguments are a float, it convert into a int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    new = a + b
    return new
