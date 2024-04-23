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
        __init__: initialization method for the class.
        width: get the width of the object.
        width.setter: set the width of th the object.
        height: get the height of the object.
        height.setter: set the height of the object.
        x: get the object x-coordinate along x-axis.
        x.setter: set the object x-coordinate along x-axis.
        y: get the object y-coordinate along y-axis
        y.setter: set the object y-coordinate along y-axis.
        area: get the area of the object.
        display: graphical representation of the object.
        __str__: string representation of the object.
        update: update the object properties in this ordr-
                id, width, height, x, y.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization method for the object.

        params id: id of the object.
        type id: id is of type integer.
        params width: width of the object.
        type width: width is of type integer.
        params height: height of the object.
        type height: height is of type integer.
        params x: x is the object position on the x-coordinate.
        type x: x is of type integer.
        params y: y is the object position on the y-coordinate.
        type y: y is of type integer.

        return: None.
        """
        super().__init__(id)
        ls = [width, height, x, y]
        for i in ls:
            if not isinstance(i, int) or isinstance(i, bool):
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
        """ A method to get the width of the object.

        params: None.
        return: None.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ A method to get the width of the object.

        params value: value of the new width.
        type value: value if of type integer.

        return: None.
        """
        if not isinstance(value, int):
            raise TypeError
        self.__width = value

    @property
    def height(self):
        """ A method to get the width of the object.

        params: None.
        return: None.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ A method to get the height of the object.

        params value: value of the new height.
        type value: value if of type integer.

        return: None.
        """
        if not isinstance(value, int):
            raise TypeError
        self.__height = value

    @property
    def x(self):
        """ A method to get the width of the object.

        params: None.
        return: None.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ A method to get the x-coordinate of the object.

        params value: value of the new height.
        type value: value if of type integer.

        return: None.
        """
        if not isinstance(value, int):
            raise TypeError
        self.__x = value

    @property
    def y(self):
        """ A method to get the width of the object.

        params: None.
        return: None.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """ A method to get the height of the object.

        params value: value of the new height.
        type value: value if of type integer.

        return: None.
        """
        if not isinstance(value, int):
            raise TypeError
        self.__y = value

    def area(self):
        """ A method that returns the area of the object

        params: None.
        return: None.
        """
        return self.__height * self.width

    def display(self):
        """ A method that display a graphical representation of
        the object.

        params: None.
        return: None.
        """
        countY = self.__y
        for j in range(countY):
            print()
        countX = self.__x
        for i in range(self.__height):
            for j in range(countX):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ A method that displays a string representation
        of the object.

        params: None.
        return lstr: lstr is a string representation of the object.
        return type: string.
        """
        lstr = "[Rectangle] " + "(" + str(self.id) + ") "
        lstr = lstr + str(self.__x) + "/" + str(self.__y)
        lstr = lstr + " - " + str(self.__width) + "/"
        lstr = lstr + str(self.__height)
        return lstr

    def update(self, *args):
        """ A method to update the value of multiple properties
        of the object in this order:
        id, width, height, x, y. The update depends on the number of
        arguments given to the function.

        params id[optional]: id of the object.
        type id: is an integer.
        params width[optional]: width of the object.
        type width: is an integer.
        params height[optional]: height of the object.
        type height: is an integer.
        params x[optional]: x-coordinate of the object.
        type x: is an integer.
        params y[optional]: y-coordinate of the object.
        type y: is an integer.

        return: None.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) >= 5:
            self.__y = args[4]
