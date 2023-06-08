#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if not roman_string:
        return 0
    romanos = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string in romanos.keys():
        return romanos.get(roman_string)
    else:
        b = 0
        for i in range(len(roman_string)):
            a = roman_string[i]
            if i == len(roman_string) - 1:
                b += romanos.get(a)
                break
            if a == 'I' and roman_string[i + 1] == 'V':
                if roman_string[i - 1] != 'I':
                    b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                    break
                b += romanos.get(a)
            elif a == 'I' and roman_string[i + 1] == 'X':
                if roman_string[i - 1] != 'I':
                    b += romanos.get(roman_string[i + 1]) - romanos.get(a)
                    break
                b += romanos.get(a)
            elif not roman_string[i] in romanos.keys():
                return
            else:
                b += romanos.get(a)
        return b
