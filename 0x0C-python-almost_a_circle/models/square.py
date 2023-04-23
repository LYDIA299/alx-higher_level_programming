#!/usr/bin/python3

"""Defines a Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherites from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor."""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Overloading str in base class."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width
    @size.setter
    def size(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.width = val
        self.height = val
