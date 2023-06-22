#!/usr/bin/python3
"""script that adds all arguments to a Python list"""


import json
import sys
sf = __import__('5-save_to_json_file').save_to_json_file
lf = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    my_list = lf(filename)
except Exception:
    my_list = []

x = 1
while x < len(sys.argv):
    my_list.append(sys.argv[x])
    x += 1

sf(my_list, filename)
