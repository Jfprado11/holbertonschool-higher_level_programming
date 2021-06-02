#!/usr/bin/python3
"""
returns a json string
into a python object
"""
import json


def from_json_string(my_str):
    """
    function that returns a json string
    into a python object
    """
    return json.loads(my_str)
