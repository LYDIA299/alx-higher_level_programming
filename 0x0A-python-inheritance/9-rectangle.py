#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a Rectangle class."""


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initializes a new Rectangle.

        Args:
           width (int): width of the new Rectangle
           height (int): height of the new Rectangle
        """
        
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Overrides the area() in the baseclass."""
        if self.__width and self.__height:
            return self.__width * self.__height

    def __str__(self):
        """String magic function."""
        if self.__width and self.__height:
            return "[{}] {}/{}".format(str(self.__class__.__name__),
                                       self.__width, self.__height)
