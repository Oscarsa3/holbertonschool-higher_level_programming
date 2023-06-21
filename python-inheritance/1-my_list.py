#!/usr/bin/python3
"""define class Mylist"""


class MyList(list):
    """print sorted method"""
    def print_sorted(self):
        print(sorted(self))
