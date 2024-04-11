#!/usr/bin/python3
""" module rectangle"""


class Rectangle:
    """ class rectangle"""

    def __init__(self, width, height):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, height):
        try:
            self.__height = int(height)
        except (TypeError, ValueError):
            if ValueError:
                print("height must be >= 0")
            else:
                print("height must be an integer")

    @width.setter
    def width(self, width):
        try:
            self.__width = int(width)
        except (TypeError, ValueError):
            if ValueError:
                print("width must be >= 0")
            else:
                print("width must be an integer")
