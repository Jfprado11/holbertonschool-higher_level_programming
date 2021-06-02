#!/usr/bin/python3
"""
a module that reads a text
in utf-8 and priting in the stadout
"""


def read_file(filename=""):
    """ a function that
    reads and print in stdout
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
