#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """ class constructor """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        if not isinstance(position, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position
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

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ returns the current area """
        return (self.__size ** 2)

    def pos_print(self):
        """ returns the position in spaces """
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """ prints a square with # """
        print(self.pos_print(), end='')
