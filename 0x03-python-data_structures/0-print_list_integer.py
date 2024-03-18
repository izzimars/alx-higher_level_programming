#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """Mylist printing function

    Args:
        my_list: The list to be printed

    Returns:
        None
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
