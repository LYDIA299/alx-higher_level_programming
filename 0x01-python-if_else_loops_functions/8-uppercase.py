#!/usr/bin/python3

def uppercase(str):
    str_len = len(str)
    result = ""
    for i in range(str_len):
        c = ord(str[i])
        if c > 90:
            c = c - 32
        result += chr(c)

    print("{}".format(result))
