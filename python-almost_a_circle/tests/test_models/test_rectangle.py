#!/usr/bin/python3
"""Unittest for class rectangle
"""
import unittest
import pycodestyle
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Test for differents cases"""
    def test_class_rectangle(self):

        # r4 = Rectangle(19, 5)
        # r4.width = -10
        # self.assertRaises(ValueError, r4.width)
        # r4.height = "2"
        # self.assertRaises(TypeError, r4.height)
        # r4.x = {}
        # self.assertRaises(TypeError, r4.x)
        # r4.y = -1
        # self.assertRaises(ValueError, r4.width)

        r2 = Rectangle(12, 8)
        self.assertAlmostEqual(r2.height, 8)
        self.assertAlmostEqual(r2.width, 12)

        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertAlmostEqual(r1.id, 12)
        self.assertAlmostEqual(r1.width, 10)
        self.assertAlmostEqual(r1.height, 2)
        self.assertAlmostEqual(r1.x, 0)
        self.assertAlmostEqual(r1.y, 0)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                    'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
