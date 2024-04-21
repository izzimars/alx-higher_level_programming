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
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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

    def test_no_arg(self):
        b1 = Base()
        b2 = Base(11)
        self.assertNotEqual(b1.id, b2.id)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_sameid(self):
        b1 = Base()
        b2 = Base(1)
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

class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    def test_inheritfrombase(self):
        self.assertEqual(Rectangle.__bases__,"(<class '__main__.Base'>,)")
    
    def test_rectinst(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_rectinst(self):
        r1 = Rectangle(10, 11)
        self.assertIsInstance(r1, Rectangle)

    def test_baseinst(self):
        self.assertIsInstance(r1, Base)

    def test_rectinst(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertEqual(6, r1.id)

    def test_widthpriv(self):
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 11, id = 6)
            r1.__width = 13

    def test_heightpriv(self):
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 11, id = 6)
            r1.__height = 13

    def test_xpriv(self):
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 11, id = 6)
            r1.__x = 13

    def test_ypriv(self):
        with self.assertRaises(AttributeError):
            r1 = Rectangle(10, 11, id = 6)
            r1.__y = 13

    def test_getwidth(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsInstance(r1.get_width(), int)

    def test_getheight(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsInstance(r1.get_width(), int)

    def test_getx(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsInstance(r1.get_width(), int)

    def test_gety(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsInstance(r1.get_y(), int)

    def test_setwidth(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsEqual(r1.set_width(10), r1.get_width())

    def test_setx(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsEqual(r1.set_x(10), r1.get_x())

    def test_sety(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsEqual(r1.set_y(10), r1.get_y())

    def test_setheight(self):
        r1 = Rectangle(10, 11, id = 6)
        self.assertIsEqual(r1.set_height(10), r1.get_height())

    def test_multiplevalues(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 11, 3, 16, 17, 18, 19, 20)


if __name__ == "__main__":
    unittest.main()
