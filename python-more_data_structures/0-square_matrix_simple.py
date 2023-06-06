#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[1]] * len(matrix)
    row = 0
    while row < len(matrix):
        a = row
        i = 0
        while i < len(matrix[row]):
            new[a] = list(map(potencia, matrix[row]))
            i += 1
        row += 1
    return new


def potencia(numero):
    return numero * numero
