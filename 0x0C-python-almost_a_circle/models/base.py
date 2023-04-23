#!/usr/bin/python3

"""Defines the Base class."""
import json



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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.
        @ list_dictionaries: a list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            json.dumps(list_dictionaries)
