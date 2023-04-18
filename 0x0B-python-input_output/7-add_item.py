#!/usr/bin/python3

"""Defines add_item function."""
import sys


if __name__ == "__main__":
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"
    alist = []
    try:
        alist = load_from_json_file(filename)
    except FileNotFoundError:
        pass
    finally:
        alist += sys.argv[1:]
        save_to_json_file(alist, filename)
