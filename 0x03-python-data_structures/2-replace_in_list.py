#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """A function that replace a list
    at a certain index with a new element

    Args:
        my_list: The list to be indexed
        idx: the index

    Returns:
        None
    """
    if (idx < 0 or idx > len(my_list)):
         return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
