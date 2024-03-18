#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """A function that prints a 2D array

    Args:
        matrix: 2D matrix to be printed

    Returns:
        None
    """
    if not matrix:
        return None
    else:
        for i in matrix:
            for j in i:
                if j == i[-1]:
                    print("{}".format(j), end='')
                else:
                    print("{}".format(j), end=' ')
            print()
