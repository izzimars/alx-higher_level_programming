#!/usr/bin/python3
"""
rectangle Module
====================

This module defines the Base class, which inherits from
the object class, it is used as a bas for other geometries.

Class:
    Base: A subclass of object a super class for other shapes.

Public Function:
    None.

"""


from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        ls = [width, height, x, y]
        for i in ls:
            if not isinstance(i, int):
                raise TypeError("{} must be an integer.".format(i))
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    @property
    def width(self):
       return self.__width
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError
        self.__width = width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError
        self.__height = height
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError
        self.__y = y
