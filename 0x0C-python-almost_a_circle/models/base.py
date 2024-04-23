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
