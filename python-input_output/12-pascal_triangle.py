#!/usr/bin/python3
"""function  that returns a list of lists of integers representing
the Pascal’s triangle"""


def pascal_triangle(n):
    """Return a matrix of integers representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    tri = [[1]]
    for i in range(n - 1):
        new = [1]
        for x in range(len(tri) - 1):
            new.append(tri[i][x] + tri[i][x + 1])
        new.append(1)
        tri.append(new)
    return tri
