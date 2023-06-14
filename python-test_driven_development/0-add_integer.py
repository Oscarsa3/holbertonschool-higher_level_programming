#!/usr/bin/python3
"""Create function than adds 2
integers a and b must be integers
or floats, otherwise raise a
TypeError exception with
the message"""


def add_integer(a, b=98):
    """Returns an integer:
    the addition of
    a and b"""

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
