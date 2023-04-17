#!/usr/bin/python3

"""Defines text-file reading function."""


def read_file(filename=""):
    """Reads a text file and prints it to stdout.
    @ filename: file to be read.
    """

    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data)
