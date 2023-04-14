#!/usr/bin/python3


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    key_bg = list(a_dictionary)[0]
    bg_val = a_dictionary[key_bg]

    for k, v in a_dictionary.items():
        if v > bg_val:
            bg_val = v
            key_bg = k
    return key_bg
