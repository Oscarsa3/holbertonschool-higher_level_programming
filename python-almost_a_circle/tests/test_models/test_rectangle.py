#!/usr/bin/python3
"""Unittest for class rectangle
"""
import unittest
import pycodestyle
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Test for differents cases"""
    def test_class_rectangle(self):
        """Test  fro this method"""
        r3 = Rectangle(1, 2)
        self.assertAlmostEqual(r3.id, 21)
        self.assertAlmostEqual(r3.x, 0)
        self.assertAlmostEqual(r3.y, 0)
        r2 = Rectangle(12, 8)
        self.assertAlmostEqual(r2.id, 22)
        self.assertAlmostEqual(r2.height, 8)
        self.assertAlmostEqual(r2.width, 12)
        self.assertAlmostEqual(r2.x, 0)
        self.assertAlmostEqual(r2.y, 0)
        a = r2.area()
        self.assertAlmostEqual(a, 96)
        self.assertRaises(TypeError, Rectangle, 4, "6")
        self.assertRaises(TypeError, Rectangle, "6", 3)
        self.assertRaises(ValueError, Rectangle, -2, 3)
        self.assertRaises(ValueError, Rectangle, 2, -3)
        self.assertRaises(ValueError, Rectangle, 0, 3)
        self.assertRaises(TypeError, Rectangle, 2, 3, "3", 1)
        self.assertRaises(TypeError, Rectangle, 2, 3, 5, [3, 6])
        self.assertRaises(ValueError, Rectangle, 2, 3, 0, -1)
        self.assertRaises(ValueError, Rectangle, 2, 3, -5, 1)
        self.assertRaises(TypeError, Rectangle, 2, 3, 5.6, 1)
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r1.id, 12)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)

    def test_to_dictionary(self):
        """Test for this method"""
        r1 = Rectangle(10, 2, 1, 9)
        self.assertAlmostEqual(r1.to_dictionary(), r1.to_dictionary())
        self.assertAlmostEqual(type(r1.to_dictionary()), dict)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                    'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
