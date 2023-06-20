#!usr/bin/python3
"""
function that returns the list attributes
and methods of object
"""


def lookup(obj):
    """Return a list of attributes and methods od obj

    args:
        obj: thefirsargument

    return:

        list attributes and methods
    """
    return dir(obj)
