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


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_inheritfrombase(self):
        self.assertEqual(str(Rectangle.__bases__), "(<class 'models.base.Base'>,)")

    def test_rectinst(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()
            print(r1)

    def test_rectinstvar(self):
        r1 = Rectangle(10, 11)
        self.assertIsInstance(r1, Rectangle)

    def test_baseinst(self):
        r1 = Rectangle(10, 11)
        self.assertIsInstance(r1, Base)

    def test_rectinstid(self):
        r1 = Rectangle(10, 11, id=6)
        self.assertEqual(6, r1.id)


    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_limit(self):
        with self.assertRaises(ValueError):
            print(Rectangle(-5, 5, 0, 0, 1).y)

    def test_height_limit(self):
        with self.assertRaises(ValueError):
            print(Rectangle(5, -5, 0, 0, 1).y)

    def test_x_limit(self):
         with self.assertRaises(ValueError):
             print(Rectangle(5, 5, -5, 0, 1).y)

    def test_y_limit(self):
        with self.assertRaises(ValueError):
            print(Rectangle(5, 5, 5, -5, 1).y)

    def test_x_typlimit(self):
        with self.assertRaises(TypeError):
            print(Rectangle(5, 5, 'l', 5, 1).y)

    def test_y_typlimit(self):
        with self.assertRaises(TypeError):
            print(Rectangle(5, 5, 5, "school", 1).y)

    def test_width_typlimit(self):
        with self.assertRaises(TypeError):
            print(Rectangle([1, 2, 3,], 10, 10, 7, 1).y)

    def test_height_typlimit(self):
        with self.assertRaises(TypeError):
            print(Rectangle(9, True, 10, 7, 1).y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)

    def test_getwidth(self):
        r1 = Rectangle(10, 11, id=6)
        self.assertIsInstance(r1.width, int)

    def test_getheight(self):
        r1 = Rectangle(10, 11, id=6)
        self.assertIsInstance(r1.height, int)

    def test_getx(self):
        r1 = Rectangle(10, 11, id=6)
        self.assertIsInstance(r1.x, int)

    def test_gety(self):
        r1 = Rectangle(10, 11, id=6)
        self.assertIsInstance(r1.y, int)

    def test_setwidth(self):
        r1 = Rectangle(10, 11, id=6)
        r1.width = 10
        self.assertEqual(10, r1.width)

    def test_setx(self):
        r1 = Rectangle(10, 11, id=6)
        r1.x = 10
        self.assertEqual(r1.x, 10)

    def test_sety(self):
        r1 = Rectangle(10, 11, id=6)
        r1.y = 100
        self.assertEqual(r1.y, 100)

    def test_setheight(self):
        r1 = Rectangle(10, 11, id=6)
        r1.height = 10
        self.assertEqual(r1.height, 10)

    def test_multiplevalues(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 11, 3, 16, 17, 18, 19, 20)
            print(r1)


if __name__ == "__main__":
    unittest.main()
