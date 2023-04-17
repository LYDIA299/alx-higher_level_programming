#!/usr/bin/python3

"""Defines a function that appends a string to the file."""


def append_write(filename="", text=""):
    """Returns the number of characters added.
    @ filename: file to add to.
    @ text: string to add to the file.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return (f.write(text))
