#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Mylist printing function

    Args:
        my_list: The list to be printed

    Returns:
        None
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]
    else:
        list_new = my_list[:]
        list_new[idx] = element
        return list_new
