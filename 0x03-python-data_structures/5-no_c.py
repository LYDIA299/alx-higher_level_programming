#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    if 'c' in my_string:
        idx = my_string.index('c')
        new_string = my_string[:idx] + my_string[idx + 1:]
    elif 'C' in my_string:
        idx = my_string.index('C')
        new_string = my_string[:idx] + my_string[idx + 1:]
    return new_string
