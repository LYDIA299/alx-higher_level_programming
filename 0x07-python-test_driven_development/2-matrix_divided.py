#!/usr/bin/python3

"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.
    Args:
        matrix (list of lists): contains int or float elements
        div (int/float): the divisor.
    Raises:
        TypeError: if the matrix contains non-numbers.
        TypeError: if the matrix contains rows of different sizes.
        TypeError: if div is not an int or float.
        ZeroDivisionError: if div is 0.
    Returns:
        A new matrix having the result of the division.
    """

    if (div == 0):
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(elt, int) or isinstance(elt, float))
                for elt in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
