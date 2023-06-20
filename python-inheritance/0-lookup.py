#!usr/bin/python3
"""function that returns the list of available
attributes and methods of an object"""


def lookup(obj):
    """Return a list of attributes and methods od obj"""
    return dir(obj)
