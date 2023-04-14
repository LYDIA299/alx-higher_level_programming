#!/usr/bin/python3

"""Defines uniq_add function."""


def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""

    if isinstance(my_list, list):
        uniq_int = []
        for i in my_list:
            if i not in uniq_int:
                uniq_int.append(i)
        sum = 0
        for i in uniq_int:
            sum += i
        return (sum)
