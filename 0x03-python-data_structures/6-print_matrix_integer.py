#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for i in matrix:
            for j in i:
                if j == i[-1]:
                    print("{}".format(j))
                else:
                    print("{}".format(j), end=' ')
