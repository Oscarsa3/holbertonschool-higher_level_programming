#!/usr/bin/python3
"""Create the function that prints
a text with 2 new lines
after each of these
characters: ., ? and :"""


def text_indentation(text):
    """Define
the
function"""

    if type(text) != str:
        raise TypeError("text must be a string")
    a = 0
    for x in text:
        if a == 1:
            x = ""
            a = 0
        if x in ['.', '?', ':']:
            a = 1
            print(f"{x}\n\n", end='')
        else:
            print(x, end='')
