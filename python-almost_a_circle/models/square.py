#!/usr/bin/python3
"""New class Square that inherits from rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """New class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y)

    def __str__(self):
        """Overrride str method"""
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.width}"
