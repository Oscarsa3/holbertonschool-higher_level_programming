#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """This class inherits from list, have a method"""
    def print_sorted(self):
        super().sort()
