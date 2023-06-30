#!/usr/bin/python3
"""Unittest for class rectangle
"""
import unittest
import pycodestyle
from models.square import Square


class Test_Square(unittest.TestCase):
    """Test for differents cases"""
    def test_class_square(self):
        s1 = Square(10, 0, 0, 12)
        self.assertAlmostEqual(s1.id, 12)
        self.assertAlmostEqual(s1.width, 10)
        self.assertAlmostEqual(s1.height, 10)
        self.assertAlmostEqual(s1.x, 0)
        self.assertAlmostEqual(s1.y, 0)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
