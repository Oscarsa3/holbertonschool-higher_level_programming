#!/usr/bin/python3
"""Define class Mylist"""


class MyList(list):
    """This class inherits from list, have a method"""
    def print_sorted(self):
        print(sorted(self))
