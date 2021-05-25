#!/usr/bin/python3
"""A module that returns the name passed
return a string with the name
if the argms wont wotk if there are not string
"""


def say_my_name(first_name, last_name=""):
    """print the argumets passed
    args:
        first_name: (str) = the first name
        last_name: (str) = the last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
