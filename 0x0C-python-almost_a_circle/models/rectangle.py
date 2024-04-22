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
    """
    Rectangle Class

    A super class of Rectangle and its functionality.

    Public Methods:
        __init__: initialization method.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization method.

        params id: id for the rectangle.
        type id: integer type.
        params y: y is the value on the y axis.
        type y: integer type.
        params width: values of the width.
        type width: integer type.
        params height: values of the heigth.
        type height: integer type.

        return: none
        """

        super().__init__(id)
        ls = [width, height, x, y, id]
        for i in ls:
            if not isinstance(i, int):
                raise TypeError
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def get_width(self):
        """ Returns the width"""

        return self.__width

    def set_width(self, width):
        """ Set the width """

        if not isinstance(width, int):
            raise TypeError
        self.width = width

    def get_height(self):
        """ Returns the width"""

        return self.__height

    def set_height(self, height):
        """ Set the width """

        if not isinstance(height, int):
            raise TypeError
        self.height = height

    def get_x(self):
        """ Returns the x value"""

        return self.__x

    def set_x(self, x):
        """ Set the x value"""

        if not isinstance(x, int):
            raise TypeError
        self.x = x

    def get_y(self):
        """ Returns the y value"""

        return self.__y

    def set_y(self, y):
        """ Set they value"""

        if not isinstance(y, int):
            raise TypeError
        self.y = y
