#!/usr/bin/python3
"""Create an class Rectangle that defines a rectangle,
Private instance attribute: width, Private instance attribute: height,
Public class attribute number_of_instances, Public class attribute
print_symbol, Public instance method: def area(), Public instance
method: def perimeter(), Static method def bigger_or_equal(rect_1, rect_2),
Class method def square(cls, size=0).
"""


class Rectangle:
    """Define Private instance attribute, Public class attribute,
    Static method,  Class method.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
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
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        Rectangle.number_of_instances += 1
        return 'Rectangle('+str(self.__width)+', '+str(self.__height)+')'

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def square(cls, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        return cls(size, size)

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
        if type(value) != int:
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
