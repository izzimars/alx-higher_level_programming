#!/usr/bin/python3
"""
base_geometry Module
====================

This module defines the MyList class, which inherits from
the built-in list class.

BaseGeometry:
    MyList: A subclass of list with additional functionality.

Public Function:
    None.

"""


class BaseGeometry:
    """
    BaseGeometry Class

    A subclass of list with additional functionality.

    Public Methods:
        None.

    """

    def area(self):
        """
        Raise an exception to show the class has not been implemented.

        This method raises an exception.

        Returns:
            None

        """

        try:
            raise Exception
        except Exception:
            print("area() is not implemented")
