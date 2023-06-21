#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""a class Rectangle that inherits from BaseGeometry and
has an init method and instantion with args width and
height"""


class Rectangle(BaseGeometry):
    """Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantion with args width and height"""

        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
