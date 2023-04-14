#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    """Replaces or adds key/value in a dictionary.

    Args:
        key: always strings
        value: will be of any type
    """

    a_dictionary[key] = value

    return a_dictionary
