#!/usr/bin/python3
def element_at(my_list, idx):
    """Get the element at the specified index in the list. 

    Args:
        my_list: The list to be indexed
        idx: the index

    Returns:
        None
    """
    if (idx >= len(my_list) or idx < 0):
        return None
    else:
        return my_list[idx]
