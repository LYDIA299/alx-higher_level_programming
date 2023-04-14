#!/usr/bin/python3

"""Defines only_diff function."""


def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in all sets but not in both."""

    return set_1 ^ set_2
