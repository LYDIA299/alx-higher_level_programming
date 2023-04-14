#!/usr/bin/python3

def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer."""

    if not isinstance(roman_string, str):
        return 0
    roman_string.upper()
    rom_ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    ret = 0
    prev_val = 0

    for i in range(len(roman_string)):
        cur_val = rom_ref[roman_string[i]]
        if cur_val > prev_val:
            ret += cur_val - 2 * prev_val
        else:
            ret += rom_ref[roman_string[i]]
        prev_val = cur_val

    return ret
