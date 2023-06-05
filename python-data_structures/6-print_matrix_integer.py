#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for i in range(len(matrix[0])):
            if i < len(matrix[0]) - 1:
                print("{:d}".format(matrix[row][i]), end=' ')
            else:
                print("{:d}".format(matrix[row][i]), end='')
        print()
