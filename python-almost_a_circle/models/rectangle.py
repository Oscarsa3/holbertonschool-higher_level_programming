#!/usr/bin/python3
"""Class Rectangle that inherits from base"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Private instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """Overriding the str method"""
        return f"""[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - {self.__width}/{self.__height}"""

    def area(self):
        """Return that returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for x in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """Update arguments to each attributes"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

        if args is not None:
            if len(args) == 1:
                super().__init__(args[0])
            if len(args) == 2:
                self.__width = args[1]
            if len(args) == 3:
                self.__height = args[2]
            if len(args) == 4:
                self.__x = args[3]
            if len(args) == 5:
                self.__y = args[4]
