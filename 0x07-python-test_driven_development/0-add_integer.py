#!/usr/bin/python3

"""Adds 2 integers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    float are typecasted to ints before addition.
    Raises:
    TypeError: if a or b is not a float or int.
    """

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
