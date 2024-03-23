#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return None
    new_list = list(a_dictionary.values())
    if value not in new_list:
        return a_dictionary
    new_dict = a_dictionary.copy()
    for i in new_dict.keys():
        if new_dict[i] == value:
            del a_dictionary[i]
    return a_dictionary
