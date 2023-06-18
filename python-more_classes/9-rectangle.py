#!/usr/bin/python3
"""Create an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Define the function"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Define init"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Define str"""
        if self.__width != 0 and self.__height != 0:
            for x in range(self.__height):
                for y in range(self.__width):
                    print("{}".format(self.print_symbol), end='')
                if x == self.height - 1:
                    print("", end='')
                else:
                    print()
        return ""

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Define a static method"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        elif rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Define a classmethod"""
        return cls(size, size)

    def __repr__(self):
        """New instance"""
        return 'Rectangle('+str(self.__width)+', '+str(self.__height)+')'

    def __del__(self):
        """Delete instance"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def height(self):
        """Property height"""
        return self.__height

    @property
    def width(self):
        """Property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Define setter width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Define setter height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
