#!/usr/bin/python3
"""A module with a
class for the base of the rest of clases
"""
import json
import os


class Base():
    """a class base for the rest"""

    __nb_objects = 0

    def __init__(self, id=None):
        """the contructor for the class base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """a list returnin into json string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """a class method writes the JSON string
        representation of list_objs to a file:
         """
        if list_objs is None:
            with open("{}.json".format(cls.__name__), "w") as file:
                json.dump([], file)
        else:
            list_dict = []
            for x in range(len(list_objs)):
                list_dict.append(list_objs[x].to_dictionary())
            serial = Base.to_json_string(list_dict)
            with open("{}.json".format(cls.__name__), "w") as file:
                file.write(serial)

    @staticmethod
    def from_json_string(json_string):
        """return the the represetantion of list into a list"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """from a file to object idk"""
        list_new = []
        if os.path.exists("{}.json".format(cls.__name__)):
            with open("{}.json".format(cls.__name__), "r") as file:
                new = Base.from_json_string(file.read())
                for x in new:
                    list_new.append(cls.create(**x))
            return list_new
        else:
            return list_new
