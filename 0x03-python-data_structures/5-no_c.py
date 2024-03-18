#!/usr/bin/python3
def no_c(my_string):
    """A function to subtituet a value in a copied version of the input list

    Args:
        my_string: A string variable.

    Returns:
        A string
    """
    new_lst = list(my_string)
    for i in new_lst:
        if i == 'c' or i == 'C':
            new_lst.remove(i)
    new_str = "".join(new_lst)
    return new_str
