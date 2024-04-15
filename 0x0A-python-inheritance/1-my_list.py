#!/usr/bin/python3
"""
MyList Module
=============

This module defines the MyList class, which inherits from
the built-in list class.

Classes:
    MyList: A subclass of list with additional functionality.

Public Function:
    None.

"""


class MyList(list):
    """
    MyList Class

    A subclass of list with additional functionality.

    Public Methods:
        print_sorted(): Print the elements of the list in ascending order.

    """

    def print_sorted(self):
        """
        Print the elements of the list in ascending order.

        This method sorts the elements of the list in ascending order
        and prints the sorted list.

        Returns:
            None

        """

        b = self[:]
        b.sort()
        print(b)
