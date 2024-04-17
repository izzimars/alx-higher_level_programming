#!/usr/bin/python3
"""
from_json_string Module
=====================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""

import json


def from_json_string(my_str):
    """
    A function that returns python representatio of a json object.

    This method returns the python equivalent of a json object.

    :params my_str: a json string.
    :type str: json string representation.

    Returns:
        python object.
    """

    return json.loads(my_str)
