#!/usr/bin/python3
"""First class base"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
