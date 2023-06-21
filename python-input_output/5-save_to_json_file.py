#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON
representation"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file"""
    with open(filename, 'w') as f:
        return f.write(json.dumps(my_obj))
