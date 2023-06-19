#!/usr/bin/python3
"""Create an empty class Rectangle that defines a rectangle
"""


class Rectangle:
    """Define class Rectangle with a constructor"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
       """Constructor with two arguments

        Set the height and with of the rectangle

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        """  
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print a rectangle with a given symbol"""
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                for y in range(self.__width):
                    print(self.print_symbol, end='')
                if x == self.height - 1:
                    print("", end='')
                else:
                    print()
        return ""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Define a static method and verify Exceptions"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new instance of Rectangle"""
        width = size
        height = size
        return cls(size, size)

    def __repr__(self):
        """Return a string that contain a new instance of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete instance and print a message"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Property to return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """This setter width checked if it's an integer"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """This setter height checked if it's an integer"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
