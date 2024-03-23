#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ A funtion that performs intersection on two list

    Args:
        1)set_1: a list type argument
        2)set_2: a list type argument

    Return:
        -]A new list item with the intersection result
    """
    new_list = list(set_1.intersection(set_2))
    return new_list
