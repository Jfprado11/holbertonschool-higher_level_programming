#!/usr/bin/python3
"""
writing in a new file
this module contains just one function
"""


def write_file(filename="", text=""):
    """
    function that writes a file or create
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
