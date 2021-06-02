#!/usr/bin/python3
"""
a function that create an python object from a
json file
"""
import json


def load_from_json_file(filename):
    """
    reads a json file and converts into an object
    """
    with open(filename, "r") as file:
        data = json.load(file)
    return data
