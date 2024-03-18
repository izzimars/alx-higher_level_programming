#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """A function to subtituet a value in a copied version of the input list

    Args:
        my_list: The list to be copied
        idx: An integer to idicate the index
        element: The value to be inserted

    Returns:
        List
    """
    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]
    else:
        list_new = my_list[:]
        list_new[idx] = element
        return list_new
