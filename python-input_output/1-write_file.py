#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)
and returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string and return the number of characters"""
    with open(filename, 'w') as f:
        return f.write(text)
