#!/usr/bin/python3
"""
is_same_class Module
====================

This module defines the is_same_class class, which inherits from
the object class.
    is_same_class: A new class without a formal base class.

Public Function:
    is_same_class: Apublic function that checks if an object
    belongs to a class.

"""


def is_same_class(obj, a_class):
    """
    Checks if the inputted object belong to the inputted class.

    This method returns a boolean true or false if the inputted
    object obj belongs as the same class as the inputted class a_class.

    :params obj: the object to be inputed for the comparison.
    :type object: instance of any class.
    :params a_class: the class name to be used for the comparison
    :type class: ...

    Returns:
        Boolean

    """

    return type(obj) is a_class
