#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    start_at = len(my_list) - 1
    for i in range(start_at, -1, -1):
        print("{:d}".format(my_list[i]))
