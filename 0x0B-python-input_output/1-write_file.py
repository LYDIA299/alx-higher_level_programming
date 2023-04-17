#!/usr/bin/python3

"""Defines write to file function."""


def write_file(filename="", text=""):
    """Returns number of characters written.
    @ filename: file to write to.
    @ text: string to put in the file.
    """

    with open(filename, 'w', encoding='utf-8') as f:
         return f.write(text)
