#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_list = list(a_dictionary.keys())
    if key in new_list:
        del a_dictionary[key]
    return a_dictionary
