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
            return []
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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        from models.rectangle import Rectangle
        from models.square import Square

        if cls is Rectangle:
            ins = Rectangle(7, 56)
        if cls is Square:
            ins = Square(34)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r') as f:
                my_list = cls.from_json_string(f.read())
                for i in range(len(my_list)):
                    my_list[i] = cls.create(**my_list[i])

        except FileNotFoundError:
            my_list = []

        return my_list
