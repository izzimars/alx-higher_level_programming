#!/usr/bin/python3
"""
student Module
====================

This module contains only a single class and no public method.

Classes:
    Student: A new class that inherits from object.

Public Function:
    None.
"""


class Student:
    """
    Student Class

    A class student containing instance method and attribute that
    define the student class.

    """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student.

        :params self: a representation of the class instance.
        :type Student: instance of class Student.

        Returns:
           None.
        """

        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
