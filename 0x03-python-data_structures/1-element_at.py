#!/usr/bin/python3
def element_at(my_list, idx):
    """A function that mimmic the way 
    indexing a function in c is

    Args:
        my_list: The list to be indexed
        idx: the index

    Returns:
        None
    """
    if (idx >= len(my_list) or idx < 0):
        return (None)
    else:
        return (my_list[idx])
