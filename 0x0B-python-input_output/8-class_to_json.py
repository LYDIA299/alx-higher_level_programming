#!/usr/bin/python3

"""Defines class_to_json function."""


def class_to_json(obj):
    """Returns the dictionary description of the obj.
    @ obj: instance of a class.
    """
    return obj.__dict__
