#!/usr/bin/python3
""" class square"""


class Square:
    """Define size"""

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """ Creat new methoCreat new method"""

        return (self.__size ** 2)
