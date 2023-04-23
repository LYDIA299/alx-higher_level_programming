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

    def update(self, *args, **kwargs):
        """Overrides the update method in the base class."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                """Looping through the arguments."""
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                    self.height = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.width = v
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v
