#!/usr/bin/python3
"""Unittest for class base
"""
import unittest
import pycodestyle
import json
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        """test for this method"""
        self.assertAlmostEqual(Base.to_json_string([]), "[]")
        self.assertAlmostEqual(Base.to_json_string(None), "[]")
        js = json.dumps([{'width': 4, 'height': 5}])
        self.assertAlmostEqual(Base.to_json_string([{'width': 4,
                                                   'height': 5}]), js)
        self.assertAlmostEqual(str, type(js))

    def test_from_json_strin(self):
        """test for this method"""
        self.assertAlmostEqual(Base.from_json_string(""), [])
        self.assertAlmostEqual(Base.from_json_string(None), [])
        js = json.loads('[{"width": 4, "height": 5}]')
        self.assertAlmostEqual(Base.from_json_string('[{"width": 4,\
                                                   "height": 5}]'), js)
        self.assertAlmostEqual(list, type(js))

    def test_save_to_file(self):
        """Test for this method"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), '[]')
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        fi1 = r1.to_dictionary()
        fi2 = r2.to_dictionary()
        filec = [fi1, fi2]
        fi3 = Rectangle.to_json_string(filec)
        with open("Rectangle.json", "r") as f:
            self.assertAlmostEqual(f.readline(), fi3)

    def test_create(self):
        """Test for this method"""
        r1 = Rectangle(3, 5, 1)
        r1_d = r1.to_dictionary()
        r2 = Rectangle.create(**r1_d)
        self.assertAlmostEqual(r1.id, 5)
        self.assertFalse(r1 == r2)
        self.assertFalse(r1 is r2)

    def test_pycodestyle_conformance(self):
        """Test that we conform to PEP8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py', 'models/rectangle.py'])
        self.assertEqual(result.total_errors, 0, "Found errors")
