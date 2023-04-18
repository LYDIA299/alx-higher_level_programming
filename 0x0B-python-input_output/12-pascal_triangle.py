#!/usr/bin/python3

"""Defines Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents the Pascal's triangle.
    @ n: number of inner lists.
    """

    if n <= 0:
        return []

    ret_list = [[1]]
    for i in range(1, n):
        cur = ret_list[-1]
        tmp = [1]
        for j in range(len(cur) - 1):
            tmp.append(cur[j] + cur[j + 1])
        tmp.append(1)
        ret_list.append(tmp)
    return ret_list
