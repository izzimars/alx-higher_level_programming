#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function that copies a listand replacaes an element  at a particular index.

    Args:
        my_list: The list to be indexed
        idx: the index
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]
    else:
        list_new = my_list[:]
        list_new[idx] = element
        return list_new
