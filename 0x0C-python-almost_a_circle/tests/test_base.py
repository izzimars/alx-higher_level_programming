#!/usr/bin/python3
"""Defines unittests for base.py.

Unittest classes:
    TestBase_instantiation - line 23
    TestBase_to_json_string - line 110
    TestBase_save_to_file - line 156
    TestBase_from_json_string - line 234
    TestBase_create - line 288
    TestBase_load_from_file - line 340
    TestBase_save_to_file_csv - line 406
    TestBase_load_from_file_csv - line 484
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_classisnone(self):
        b1 = Base()
        self.assertIsNotNone(b1.id)

    def test_classisint(self):
        b1 = Base()
        self.assertIs(int, type(b1.id))

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_arginnit(self):
        b1 = Base(9)
        self.assertEqual(9, b1.id)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_sameid(self):
        b1 = Base()
        b2 = Base(8)
        self.assertEqual(b1.id, b2.id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

class JsonConversionTests(unittest.TestCase):
    """Unit tests for testing JSON conversion with the Base class."""

    def test_baseex_json(self):
        json_string = Base.to_json_string({})
        self.assertEqual(json_string, "[]")

    def test_baseexone_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        json_string = (Base.to_json_string(r1.to_dictionary()))
        expected = (json.dumps({"id": 1, "width": 10, "x": 2, "height": 7, "y": 8}))
        json_string = json.loads(json_string)
        expected = json.loads(expected)
        self.assertEqual(json_string, expected)

    def test_baseextwo(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]") 

if __name__ == "__main__":
    unittest.main()
