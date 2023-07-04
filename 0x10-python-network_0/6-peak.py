#!/usr/bin/python3
"""
Finds a peak of a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
         list_of_integers(int)
    Returns: peak number or None
    """

    size = len(list_of_integers)
    if size == 0:
        return None

    low = 0
    high = size - 1

    while low < high:
        mid = (low + high) // 2
        cur = list_of_integers[mid]
        next_val = list_of_integers[mid + 1]

        if cur < next_val:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
