#!/usr/bin/python3
""" class square"""


class Square:
    """Define size"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Creat method that returns the current square area"""

        return (self.__size ** 2)

    def my_print(self):
        """Create method that prints in stdout the square with the character"""

        if self.__size == 0:
            print()
        for a in range(self.__position[1]):
            print()
        for x in range(self.__size):
            for b in range(self.__position[0]):
                print("_", end="")
            for y in range(self.__size):
                print("#", end="")
            print()
