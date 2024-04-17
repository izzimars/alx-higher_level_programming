#!/usr/bin/python3
"""
add_item.py Module
==================

Public Function:
    is_kind_of_class: Apublic function that checks if an object
    belongs to the same kind of class or subclass.

"""

import sys

if __name__ == "__main__":
    lfjf = __import__('6-load_from_json_file').load_from_json_file
    stjf = __import__('5-save_to_json_file').save_to_json_file

    try:
        items = lfjf("add_item.json")
    except FileNotFoundError:
        items = []
    lst = sys.argv[1:]
    for i in lst:
        items.append(i)
    stjf(items, "add_item.json")
