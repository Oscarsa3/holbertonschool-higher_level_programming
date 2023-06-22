#!/usr/bin/python3
"""class Student that defines a student by first_name,
last_name and age"""


class Student:
    """Define first_name, last_name and age"""
    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        try:
            new = dict(filter(lambda e: e[0] in attrs, self.__dict__.items()))
            return new
        except Exception:
            return self.__dict__

    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance"""
        remplazo = self.__dict__
        return remplazo.update(json)
