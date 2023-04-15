#!/usr/bin/python3

"""Defines MyList class."""


class MyList(list):
    """It inherits from list clase 'built-in'."""

    def print_sorted(self):
        print("{}".format(sorted(self)))
