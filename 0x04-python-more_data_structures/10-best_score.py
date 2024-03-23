#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    if len(a_dictionary) == 0:
        return None
    new_list = list(a_dictionary.keys())
    maxi = 0
    max_index = 0
    for i in new_list:
        if maxi < a_dictionary[i]:
            maxi = a_dictionary[i]
            max_index = i
    return max_index
