#!/usr/bin/python3
"""
class_to_json Module
====================

Public Function:
    is_kind_of_class: A public function that returns the attribute
    of the class of an object.

"""


def class_to_json(obj):
    """
    A function that returns a dictionary.

    This method returns a dictionary that contains the attribute of
    the argumnet class and its datatype. The dictionary is converted
    to json object.

    :params my_obj: a python object.
    :type object: python object, positional arguments.

    Returns:
        A dict datatype.
    """

    all_att = dir(obj)
    attr = [i for i in all_att if not callable(getattr(obj, i))]
    attr = [i for i in attr if not i.startswith("__")]
    attr = {i: getattr(obj, i) for i in attr}
    return attr
