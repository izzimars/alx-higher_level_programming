#!/usr/bin/python3
"""
read_file Module
================

This module defines the is_kind_of_class class, which inherits from
the object class.
    is_kind_of_class: A new class without a formal base class.

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""


def read_file(filename=""):
    """
    A function that reads a text file.

    This method reads a file and print it out to the standard
    output.

    :params filename: a computer file.
    :type file: mostly a .txt file or any kind of file.

    Returns:
        None


    """

    with open(filename, "r", encoding="utf-8") as txt:
        for line in txt:
            print(line)
