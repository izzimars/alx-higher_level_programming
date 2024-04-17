#!/usr/bin/python3
"""
append_write Module
===================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""


def append_write(filename="", text=""):
    """
    A function that writes a text to the end of  a file.

    This method reads a file and print it out to the standard
    output.

    :params filename: a computer file.
    :type file: mostly a .txt file or any kind of file.
    :params tsxt: a string of words to be written to filename.
    :type str: a string.

    Returns:
        None
    """

    with open(filename, 'a', encoding="utf-8") as txt:
        return txt.write(text)
