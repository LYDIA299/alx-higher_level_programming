#!/usr/bin/python3

"""Defines a MyInt class that inherits from 'int' built-in class."""


class MyInt(int):
    """Has only methods."""

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
