#!/usr/bin/python3
"""
A modules that holds a function
that write in a text some json represetation
"""
import json


def save_to_json_file(my_obj, filename):
    """ write a string respresetation in json
    into filename
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)
