#!/usr/bin/python3

""" Define a rectangle """


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
        width (int): width of a rectangle.
        height (int): height of a rectangle.
        """

        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')

        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError('width must be an integer')
        if val < 0:
            raise ValueError('width must be >= 0')
        self.__width = val

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError('height must be an integer')
        if val < 0:
            raise ValueError('height must be >= 0')
        self.__height = val

    def area(self):
        """Calculates the area of a rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Returns the diagram of a rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ('')
        rectangle = ''
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += '#'
            if column < self.__height - 1:
                rectangle += "\n"

        return (rectangle)

    def __repr__(self):
        """Recreates a new instance of a rectangle."""

        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))
