#!/usr/bin/python3
"""
base Module
====================

This module defines the Base class, which inherits from
the object class, it is used as a bas for other geometries.

Class:
    Base: A subclass of object a super class for other shapes.

Public Function:
    None.

"""


import json


class Base:
    """
    Base Class

    A super class of other geometry with additional functionality.

    Public Methods:
        __init__: initialization method.

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization method.

        params id: expect an integer.

        return: none
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ converts a dictionary into a json notation.

        params list_dictionary: a dictionary holding the represenation
                                of a normal object.
        params type: python dictionary.
        return value: json represenation of the object.
        return type: json.

        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        if (json_string is None or len(json_string) == 0):
            return []
        else:
            return json.loads(json_string)
