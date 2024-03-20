#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    suma = 0
    num = 0
    for i in (my_list):
        suma = suma + (i[0] * i[1])
        num = num + i[1]
    argv = suma / num
    return argv
