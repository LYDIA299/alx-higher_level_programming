#!/usr/bin/python3

"""Defines a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class contructor.
        @ width: width of the rectangle
        @ height: height of the rectangle.
        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns area of a Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the Rectangle with '#' character."""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            print('#' * self.__width)

    def __str__(self):
        """Overrides str in the base class."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute."""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                """Looping through the arguments."""
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            """Key-worded arguments."""
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        """Returns a dictionary representation of a Rectangle."""
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width
            }
