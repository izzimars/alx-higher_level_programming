#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = set(my_list)
    new_list = list(new_list)
    summax = 0
    for i in new_list:
        summax = summax + i
    return summax
