#!/usr/bin/python3
"""define class mylist that print sorted
in ascending sort"""


class MyList(list):
    """print sorted method"""

    def print_sorted(self):
        print(sorted(self))
