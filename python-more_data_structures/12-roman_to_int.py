#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    ro = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rom = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    romanos = {**ro, **rom}
    if roman_string in romanos.keys():
        return romanos.get(roman_string)
    else:
        b = 0
        i = 0
        while i < len(roman_string):
            a = roman_string[i]
            if i == len(roman_string) - 1:
                b += romanos.get(a)
            elif roman_string[i: i + 2] in romanos.keys():
                a = roman_string[i: i + 2]
                b += romanos.get(a)
                a = roman_string[i]
                i += 1
            elif not roman_string[i] in romanos.keys():
                return
            else:
                b += romanos.get(a)
            i += 1
        return b
