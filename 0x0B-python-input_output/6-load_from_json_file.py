#!/usr/bin/python3

"""Defines object-create function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”.
    @ filename: file containing JSON.
    """

    with open(filename) as f:
        """json.loads(f.read())."""
        return json.load(f)
