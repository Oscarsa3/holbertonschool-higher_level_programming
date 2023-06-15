#!/usr/bin/python3
"""Create function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Define the function"""

    error = "matrix must be a matrix (list of lists) of integers/floats"
    error2 = "Each row of the matrix must have the same size"
    if type(matrix) != list:
        raise TypeError(error)
    for x in range(len(matrix)):
        if type(matrix[x]) != list:
            raise TypeError(error)
        if x != len(matrix) - 1:
            if len(matrix[x]) != len(matrix[x + 1]):
                raise TypeError(error2)
        for k in range(len(matrix[x])):
            if type(matrix[x][k]) not in [int, float]:
                raise TypeError(error)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = matrix.copy()
    for i in range(len(matrix)):
        new[i] = list(map(lambda x: round(x / div, 2), matrix[i]))
    return new
