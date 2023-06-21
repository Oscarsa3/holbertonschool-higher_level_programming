#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry and
has an init method and instantion with args width and
height"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantion with args width and height"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def __str__(self):
        """Return a function of the class"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        """Print a function of the class"""
        print(f"[Rectangle] {self.__width}/{self.__height}")

    def area(self):
        """Return the area of the geometry"""
        return self.__width * self.__height
