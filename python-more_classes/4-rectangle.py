#!/usr/bin/python3
"""Create an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Define the function"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                for y in range(self.__width):
                    print("#", end='')
                if x == self.height - 1:
                    print("", end='')
                else:
                    print()
        return ""

    def __repr__(self):
        n = 'Rectangle(' + str(self.__width) + ',' + str(self.__height) + ')'
        return n

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
