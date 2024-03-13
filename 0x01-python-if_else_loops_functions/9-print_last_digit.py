#!/usr/bin/python3
def print_last_digit(number):
    if (number >= 0):
        lst = number % 10
    if (number < 0):
        lst = number % -10
        lst = lst * -1
    print("{}".format(lst), end="")
    return (lst)
