#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_string = roman_string.upper()
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string in romanos.keys():
        return romanos.get(roman_string)
    else:
        b = 0
        i = 0
        while i < len(roman_string):
            a = roman_string[i]
            if i == len(roman_string) - 1:
                b += romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'V':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'X':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'L':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'C':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'D':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            elif roman_string[i] == 'I' and roman_string[i + 1] == 'M':
                b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                break
            b += romanos.get(a)
            i += 1
    return int(b)
