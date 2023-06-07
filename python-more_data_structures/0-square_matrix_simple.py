#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[1]] * len(matrix)
    i = 0
    while i < len(matrix):
        new[i] = list(map(lambda x: x ** 2, matrix[i]))
        i += 1
    return new
