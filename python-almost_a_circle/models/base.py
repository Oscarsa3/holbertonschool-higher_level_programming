#!/usr/bin/python3
"""First class base"""


class Base:
    """Our class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Define our id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            Base.id = Base.__nb_objects
