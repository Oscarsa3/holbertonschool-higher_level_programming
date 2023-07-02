#!/usr/bin/python3
"""Unittest for class rectangle
"""
import unittest
import pycodestyle
from models.square import Square


class Test_Square(unittest.TestCase):
    """Test for differents cases"""
    def test_class_square(self):
        s2 = Square(5)
        self.assertAlmostEqual(s2.id, 29)
        self.assertAlmostEqual(s2.area(), 25)
        self.assertAlmostEqual(s2.width, 5)
        self.assertAlmostEqual(s2.height, 5)
        self.assertAlmostEqual(s2.x, 0)
        self.assertAlmostEqual(s2.y, 0)

        s1 = Square(10, 0, 0, 12)
        self.assertAlmostEqual(s1.id, 12)
        self.assertAlmostEqual(s1.width, 10)
        self.assertAlmostEqual(s1.height, 10)
        self.assertAlmostEqual(s1.x, 0)
        self.assertAlmostEqual(s1.y, 0)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py',
                                   'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
