#!/usr/bin/python3
"""a module that hols a
a function that appends some text to the file
"""


def append_write(filename="", text=""):
    """function that appends
    a text to a file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
