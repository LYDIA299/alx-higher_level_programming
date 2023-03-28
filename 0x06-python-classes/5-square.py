#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """ class constructor """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """ gets the value of size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ returns the current area """
        return (self.__size ** 2)

    def my_print(self):
        """ prints a square with # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)
