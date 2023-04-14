#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2."""

    new_dictionary = {}
    for el in list(a_dictionary):
        new_dictionary[el] = a_dictionary[el] * 2

    return new_dictionary
