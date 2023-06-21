#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """appends a string and return the number of characters"""
    with open(filename, 'a') as f:
        return f.write(text)
