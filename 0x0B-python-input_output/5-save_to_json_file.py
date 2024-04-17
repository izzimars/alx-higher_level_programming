#!/usr/bin/python3
"""
save_to_json_file Module
========================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""

import json


def save_to_json_file(my_obj, filename):
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

    with open("filename", "w") as txt:
        json.dump(my_obj, txt)
