#!/usr/bin/python3
"""define class mylist that print sortedin ascending
sort, this class only has a method"""


class MyList(list):
    """this class has Print_sorted method"""

    def print_sorted(self):
        """This method Print a list sorted"""

        print(sorted(self))
