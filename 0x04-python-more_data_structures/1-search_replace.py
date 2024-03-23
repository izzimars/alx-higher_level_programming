#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            ind = new_list.index(search)
            new_list[ind] = replace
    return new_list
