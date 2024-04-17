#!/usr/bin/python3
"""
to_json_string Module
=====================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""

import json


def to_json_string(my_obj):
    """
    A function that returns json representatio of an object.

    This method returns the json euivalent of  pthon object.

    :params my_obj: a computer file.
    :type object: mostly a .txt file or any kind of file.

    Returns:
        JSON object.
    """

    return json.dumps(my_obj)
