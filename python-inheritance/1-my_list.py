#!/usr/bin/python3
"""class MyList that inherits from list and has a
public instance method that prints the
list but sorted"""


class MyList(list):
    """This class inherits from list, have a method"""

    def print_sorted(self):
        """Return the list but sorted"""

        print(sorted(self))
