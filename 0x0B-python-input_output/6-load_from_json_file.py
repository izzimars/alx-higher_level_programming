#!/usr/bin/python3
"""
load_to_json_file Module
========================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""

import json


def load_from_json_file(filename):
    """
    A function that writes a json object into a file.

    This method returns the erite the json equivalent of a python
    inside a file.

    :params my_obj: a python object.
    :type object: python object, positional arguments.
    :params filename: a file to write the json equivalent object.
    :type file: a computer file mostly a .txt file, a positional
    argument.

    Returns:
        None.
    """

    with open(filename, "r") as txt:
        jsondata = txt.read()
        return json.loads(jsondata)
