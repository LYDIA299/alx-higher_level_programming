#!/usr/bin/python3

"""Defines JSON function."""
import json


def to_json_string(my_obj):
    """Returns JSON representation of an object.
    @ my_obj: object to convert.
    """

    return (json.dumps(my_obj)
