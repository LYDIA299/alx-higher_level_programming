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

        for el in [width, height, x, y]:
            if type(el) != int:
                raise TypeError(f"{el} must be an integer")
        for el in [width, height]:
            if el <= 0:
                raise ValueError(f"{el} must be > 0")
        for el in [x, y]:
            if el < 0:
                raise ValueError(f"{el} must be >=0")

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
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        self.__y = val
