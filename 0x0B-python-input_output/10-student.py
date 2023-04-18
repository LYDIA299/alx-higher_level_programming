#!/usr/bin/python3

"""Defines Student class."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Initialization."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student."""
        if isinstance(attrs, list) and (isinstance(x, str) for x in attrs):
            ret_dict = {}
            for x in attrs:
                if hasattr(self, x):
                    ret_dict[x] = getattr(self, x)
            return ret_dict
        else:
            return self.__dict__
