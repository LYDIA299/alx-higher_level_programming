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


"""Defines a Rectangle class."""


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Constructor."""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
