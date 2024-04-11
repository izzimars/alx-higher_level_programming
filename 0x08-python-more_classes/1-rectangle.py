#!/usr/bin/python3
""" module rectangle"""


class Rectangle:
    """ class rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @width.setter
    def width(self, width):
            if not isinstance(width, int):
                raise TypeError("width must be >= 0")
            if width < 0:
                raise ValueError("width must be >= 0")
            self.__width = width
