#!/usr/bin/python3
"""Unittest for class rectangle
"""
import unittest
import pycodestyle
from unittest import mock
import io
from unittest.mock import patch
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Square(unittest.TestCase):
    """Test for differents cases"""
    def test_class_square(self):
        """Test for this method"""
        s2 = Square(5)
        self.assertAlmostEqual(s2.id, 41)
        self.assertAlmostEqual(s2.area(), 25)
        self.assertAlmostEqual(s2.width, 5)
        self.assertAlmostEqual(s2.height, 5)
        self.assertRaises(TypeError, Square, "4")
        self.assertRaises(TypeError, Square, 1, "4")
        self.assertRaises(TypeError, Square, 1, 5, "8")
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(ValueError, Square, 4, -2)
        self.assertRaises(ValueError, Square, 4, 8, -2)
        self.assertRaises(ValueError, Square, 0)
        self.assertAlmostEqual(s2.x, 0)
        self.assertAlmostEqual(s2.y, 0)
        s1 = Square(10, 0, 0, 12)
        self.assertAlmostEqual(s1.id, 12)
        self.assertAlmostEqual(s1.width, 10)
        self.assertAlmostEqual(s1.height, 10)
        self.assertAlmostEqual(s1.x, 0)
        self.assertAlmostEqual(s1.y, 0)

    def test_str(self):
        """Test for this method"""
        s1 = Square(4, 2, 1, 15)
        self.assertAlmostEqual(s1.area(), 16)
        with mock.patch("sys.stdout", new=io.StringIO()) as f:
            print(s1)
        assert f.getvalue() == "[Square] (15) 2/1 - 4\n"

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py',
                                   'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
