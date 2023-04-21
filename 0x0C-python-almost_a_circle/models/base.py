#!/usr/bin/python3

"""Defines the Base class."""


class Base():
    """Base class for all other classes in this project."""

    __nb_objects = 0
    def __init__(self, id=None):
        """class constructor.
        @ id(int): id for objects.
        """

        if (id is None):
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
