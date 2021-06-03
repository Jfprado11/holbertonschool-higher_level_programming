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

    def to_json(self, attrs=None):
        """function that returs a vars
        to a return a diccionary of an object
        """
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            a_dict = {}
            for x in attrs:
                for d in self.__dict__.keys():
                    if d == x:
                        a_dict[d] = self.__dict__[d]
            return a_dict
        else:
            return vars(self)

    def reload_from_json(self, json):
        for d in json.keys():
            if d == "first_name":
                self.first_name = json[d]
            if d == "last_name":
                self.last_name = json[d]
            if d == "age":
                self.age = json[d]
