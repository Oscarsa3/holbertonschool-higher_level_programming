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
        self.height = value

    def __str__(self):
        """Overrride str method"""
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update arguments to each attributes"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        if args is not None:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]

    def to_dictionary(self):
        """return the dictionary representation of a class"""
        return {"id": self.id, "x": self.x, "size": self.width, "y": self.y}
