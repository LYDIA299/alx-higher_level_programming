#!/usr/bin/python3

"""Defines JSON_to_object function."""
import json


def from_json_string(my_obj):
    """Returns object represented by JSON string.
    @ my_obj: string to convert.
    """

    return (json.loads(my_obj))
