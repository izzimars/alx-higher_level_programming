#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """My list printing function

    Args:
        my_list:an integer of list

    Returns:
        None
    """
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
