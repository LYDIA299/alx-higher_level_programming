#!/usr/bin/python3

"""Defines a function that add attributes to the object."""


def add_attribute(obj, attr_name, attr_value):
    """
    @ obj: object to add attributes on.
    @ attr_name: name of the attribute
    @ attr_value: value of the attribute
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr_name] = attr_value
