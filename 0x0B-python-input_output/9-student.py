#!/usr/bin/python3
"""
a class student
defined with some atributes and a method
"""


class Student:
    """
    a class with the atributes:
        first_name(str) : the first name of the class student
        last_name(str) : the last name of the class student
        age(str) : the age of the student
    a method witch returns a dict
    """

    def __init__(self, first_name, last_name, age):
        """the initialization of the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that returs a vars
        to a return a diccionary of an object
        """
        diction = vars(self)
        return diction
