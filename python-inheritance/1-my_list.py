#!/usr/bin/python3
"""define class mylist that print sorted
in ascending sort"""


class MyList(list):
    """Print_sorted method"""
    def print_sorted(self):
        """Print a list sorted"""
        print(sorted(self))
