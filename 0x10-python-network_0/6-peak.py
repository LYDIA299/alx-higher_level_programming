#!/usr/bin/python3
""" finds the peak from unsorted integers"""

def find_peak(list_of_integers):
    """finds the peak"""

    if list_of_integers is None or list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    low = 0
    high = size - 1

    while low < high:
        mid = (low + high) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            high = mid
        else:
            low = mid + 1

    return list_of_integers[high]
