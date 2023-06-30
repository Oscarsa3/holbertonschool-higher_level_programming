#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import pycodestyle
from models.base import Base


class Test_Base(unittest.TestCase):
    """Test for differents cases"""
    def test_class_Base(self):
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertAlmostEqual(b2.id, 2)
        b3 = Base()
        self.assertAlmostEqual(b3.id, 3)
        b4 = Base(23)
        self.assertAlmostEqual(b4.id, 23)
        b5 = Base(2)
        self.assertAlmostEqual(b5.id, 2)
        b6 = Base()
        self.assertAlmostEqual(b6.id, 4)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
