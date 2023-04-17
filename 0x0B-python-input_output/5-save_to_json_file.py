#!/usr/bin/python3

"""Defines save_to_json_file function."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a file using JSON.
    @ my_obj: JSON string.
    @ filename: file to write to.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
