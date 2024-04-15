#!/usr/bin/python3
"""
is_kind_of_class Module
====================

This module defines the is_kind_of_class class, which inherits from
the object class.
    is_kind_of_class: A new class without a formal base class.

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""


def is_kind_of_class(obj, a_class):
    """
    Checks if the inputted object belong to the inputted class or is a
    subclass.

    This method returns a boolean true or false if the inputted
    object obj belongs as the same class as the inputted class a_class.

    :params obj: the object to be inputed for the comparison.
    :type object: instance of any class.
    :params a_class: the class name to be used for the comparison
    :type class: ...

    Returns:
        Boolean

    """

    return isinstance(obj, a_class)
