#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a Rectangle"""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
           width (int): width of the new Rectangle
           height (int): height of the new Rectangle
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Overrides the area() in the baseclass."""
        return self.__width * self.__height

    def __str__(self):
        """String magic function.
        ret_str = "[" + str(self.__class__.__name__) + "]"""
        ret_str = "[Rectangle]"
        ret_str += " {}/{}".format(self.__width, self.__height)
        return ret_str
