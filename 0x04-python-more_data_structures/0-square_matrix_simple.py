#!/usr/bin/python3

"""Defines square_matrix function."""


def square_matrix_simple(matrix=[]):
    """Returns a new matrix with square values."""

    if isinstance(matrix, list) and isinstance(matrix[0], list):
        """Another way [[col ** 2 for col in row] for row in matrix] ."""
        return [list(map(lambda x: x ** 2, [c for c in r])) for r in matrix]
