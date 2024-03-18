#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """A function that prints a list in reverse order.

    Args:
        my_list: The list to be printed

    Returns:
        None
    """
    indx = len(my_list) - 1
    while (indx >= 0):
        print("{:d}".format(my_list[indx]))
        indx = indx - 1
