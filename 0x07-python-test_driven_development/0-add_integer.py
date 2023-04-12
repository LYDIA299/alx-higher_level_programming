#!/usr/bin/python3

"""Adds 2 integers."""

def add_integer(a, b=98):
    """Return the integer addition of a and b.
    float are typecasted to ints before addition.
    Raises:
    TypeError: if a or b is not a float or int.
    """

    if(type(a) not in [int, float]):
        raise TypeError("a must be an integer")
    if(type(b) not in [int, float]):
        raise TypeError("b must be an integer")
    if(type(a) == float):
        a = int(a)
    if(type(b) == float):
        b = int(b)

    return (a + b)
