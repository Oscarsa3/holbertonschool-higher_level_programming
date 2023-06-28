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

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string representation de list_objs to a file"""
        filename = f"{cls.__name__}.json"

        if list_objs is None:
            es = []
        else:
            es = []
            for i in list_objs:
                es.append(i.to_dictionary())
        with open(filename, 'w') as f:
            return f.write(cls.to_json_string(es))
