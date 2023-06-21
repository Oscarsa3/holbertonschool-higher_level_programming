#!/usr/bin/python3
"""a class Square that inherits from Rectangle,
size must be private and must be a positive integer and
the area() must be implemented"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Implementation of the class Square"""

    def __init__(self, size):
        """Size must be private and positive integer"""
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Return the area"""
        return self.__size * self.__size 
