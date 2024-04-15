#!/usr/bin/python3
"""
Returns the list of available attributes and methods of an object.


:param obj: The object to checks its property.
:type obj: object.
:rtype: list.
"""


def lookup(obj):
    """returns the list of available attributes"""
    return dir(obj)
