#!/usr/bin/python3
"""function that returns True if the object is an instance
of a class, otherwise False"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a clas"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
