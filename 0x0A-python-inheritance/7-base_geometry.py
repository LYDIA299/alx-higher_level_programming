#!/usr/bin/python3

"""Defines a class."""


class BaseGeometry():
    """Empty class."""

    def area(self):
        """Instance method."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
