#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """A function that returns the square of a 2 dimensional matrix

    Args:
       1)List

    Return:
        1)List
    """
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[i][j] ** 2)
    return new_matrix
