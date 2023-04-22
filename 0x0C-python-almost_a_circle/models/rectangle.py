#!/usr/bin/python3

"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class contructor.
        @ width: width of the rectangle
        @ height: height of the rectangle.
        """

        if type(x) != int:
            raise TypeError(f"{x} must be an integer")
        if x < 0:
            raise ValueError(f"{x} must be >= 0")

        if type(y) != int:
            raise TypeError(f"{y} must be an integer")
        if y < 0:
            raise ValueError(f"{y} must be >= 0")

        if type(width) != int:
            raise TypeError(f"{width} must be an integer")
        if width <= 0:
            raise ValueError(f"{width} must be > 0")

        if type(height) != int:
            raise TypeError(f"{height} must be an integer")
        if height <= 0:
            raise ValueError(f"{height} must be > 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(width) != int:
            raise TypeError(f"{width} must be an integer")
        if width <= 0:
            raise ValueError(f"{width} must be > 0")
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(height) != int:
            raise TypeError(f"{height} must be an integer")
        if height <= 0:
            raise ValueError(f"{height} must be > 0")
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(x) != int:
            raise TypeError(f"{x} must be an integer")
        if x < 0:
            raise ValueError(f"{x} must be >= 0")
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(y) != int:
            raise TypeError(f"{y} must be an integer")
        if y < 0:
            raise ValueError(f"{y} must be >= 0")
        self.__y = val
