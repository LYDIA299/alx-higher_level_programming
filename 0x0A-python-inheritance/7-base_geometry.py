#!/usr/bin/python3

"""Defines a class."""


class BaseGeometry():
    """Empty class."""

    def area(self):
        """Instance method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
