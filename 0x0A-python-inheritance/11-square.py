#!/usr/bin/python3
"""Defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size):
        """Initializes a new square instance.
        @size: must be a positive integer
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Overrides the area method in the baseclass."""
        return self.__size ** 2

    def __str__(self):
        """Magic function string representation of the class."""
        return f"[Square] {self.__size}/{self.__size}"
