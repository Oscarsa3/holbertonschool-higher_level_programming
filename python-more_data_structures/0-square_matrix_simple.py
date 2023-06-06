#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[1]] * len(matrix)
    for row in range(len(matrix)):
        a = row
        for i in range(len(matrix[row])):
            new[a] = list(map(lambda x: x ** 2, matrix[row]))
    return new
