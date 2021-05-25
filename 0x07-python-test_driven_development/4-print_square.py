#!/usr/bin/python3
"""module to print a square
just can pass integers numbers
if the not intger passed print an error raise
"""


def print_square(size):
    """a function thta print a squere made by '#'
    if size is not a int, raise a TypeError
    if size is less than 0 raise a ValueError
    args:
        size (int) = the size of the squeare
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        for i in range(size):
            print("#", end="")
        print()
