#!/usr/bin/python3
def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.


    :param obj: The object to checks its property.
    :type obj: object.
    :rtype: list.
    """
    return dir(obj)
