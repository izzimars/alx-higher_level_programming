#!/usr/bin/python3
"""
square Module
====================

This module defines the Base class, which inherits from
the rectangle class, it is used as a bas for other geometries.

Class:
    Base: A subclass of object a super class for other shapes.

Public Function:
    None.

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square Class a sub class of rectangle.
    A sub class of Rectangle and its functionality.
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

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialization method for the object.

        params id: id of the object.
        type id: id is of type integer.
        params size: size of the object.
        type size: size is of type integer.
        params x: x is the object position on the x-coordinate.
        type x: x is of type integer.
        params y: y is the object position on the y-coordinate.
        type y: y is of type integer.

        return: None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ A method that displays a string representation
        of the object.

        params: None.
        return lstr: lstr is a string representation of the object.
        return type: string.
        """
        lstr = "[Square] " + "(" + str(self.id) + ") "
        lstr = lstr + str(self.x) + "/" + str(self.y)
        lstr = lstr + " - " + str(self.width)
        return lstr

    @property
    def size(self):
        """ A method to get the size of the object.

        params: None.
        return: None.
        """
        return self.width

    @size.setter
    def size(self, value):
        """ A method to set the size of the object.

        params value: value of the new width.
        type value: value if of type integer.

        return: None.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ A method to update the value of multiple properties
        of the object in this order:
        id, width, height, x, y. The update depends on the number of
        arguments given to the function.

        params id[optional]: id of the object.
        type id: is an integer.
        params size[optional]: size of the object.
        type size: is an integer.
        params x[optional]: x-coordinate of the object.
        type x: is an integer.
        params y[optional]: y-coordinate of the object.
        type y: is an integer.

        return: None.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
            self.height = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for i in kwargs:
            if str(i) == "id" and len(args) < 1:
                self.id = kwargs[i]
            if str(i) == "size" and len(args) < 2:
                self.width = kwargs[i]
                self.height = kwargs[i]
            if str(i) == "x" and len(args) < 4:
                self.x = kwargs[i]
            if str(i) == "y" and len(args) < 5:
                self.y = kwargs[i]

    def to_dictionary(self):
        """ THis method returns the dictionary representation
        of a Square

        params: None.
        return: None.
        """
        ldict = {}
        ldict["id"] = self.id
        ldict["size"] = self.width
        ldict["x"] = self.x
        ldict["y"] = self.y
        return ldict
