#!/usr/bin/python3
"""
write_file Module
=================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""


def write_file(filename="", text=""):
    """
    A function that writes a text into a file.

    This method reads a file and print it out to the standard
    output.

    :params filename: a computer file.
    :type file: mostly a .txt file or any kind of file.
    :params tsxt: a string of words to be written to filename.
    :type str: a string.

    Returns:
        None
    """

    with open(filename, 'w', encoding="utf-8") as txt:
        return txt.write(text)
