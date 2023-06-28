#!/usr/bin/python3
"""New class Square that inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """Overrride str method"""
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"
