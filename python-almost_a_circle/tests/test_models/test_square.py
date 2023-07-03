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
        self.assertAlmostEqual(s2.id, 37)
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

    def test_save_to_file(self):
        """Test for this method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        r3 = Rectangle(10, 7, 2, 8)
        r4 = Rectangle(2, 4)
        Rectangle.save_to_file([r3, r4])
        fi1 = r3.to_dictionary()
        fi2 = r4.to_dictionary()
        filec = [fi1, fi2]
        fi3 = Rectangle.to_json_string(filec)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), fi3)
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        s3 = Square(4, 2, 7)
        s4 = Square(5)
        Square.save_to_file([s3, s4])
        ss1 = s3.to_dictionary()
        ss2 = s4.to_dictionary()
        s3 = Square.to_json_string([ss1, ss2])
        with open("Square.json", "r") as f:
            self.assertAlmostEqual(f.readline(), s3)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py',
                                   'tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
