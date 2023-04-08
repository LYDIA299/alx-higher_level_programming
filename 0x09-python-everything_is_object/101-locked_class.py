#!/usr/bin/python3

""" Creating a class. """


class LockedClass:
    """ Prevents the user from dynamically creating new instances. """
    __slots__ = 'first_name'

    def __init__(self, first_name=None):
        """Constructor."""
        self.first_name = first_name
