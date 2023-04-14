#!/usr/bin/python3

"""Defines a search_replace function."""


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list.

    Args:
        my_list: initial list.
        search: element to replace.
        replace: new element.
    """

    if isinstance(my_list, list):
        return list(map(lambda el: replace if el == search else el, my_list))
