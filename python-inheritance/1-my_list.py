#!/usr/bin/python3
# by: Oscarsa3
"""define class mylist that print sortedin ascending
sort, this class only has a method"""


class MyList(list):
    """Has a method"""
    def print_sorted(self):
        """Print a list sorted and return list without sort"""
        print(sorted(self))
