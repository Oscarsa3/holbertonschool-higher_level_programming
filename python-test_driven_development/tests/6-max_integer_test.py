#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define test about max_integer() function"""

    def test_max(self):
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([23, 65, 789]), 789)
        self.assertAlmostEqual(max_integer([0, 4565, 34, 5, 876]), 4565)

    def test_true(self):
        self.assertTrue(max_integer([2, 5, 6]))

    def test_none(self):
        self.assertIsNone(max_integer())

    def test_notnone(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_AorB(self):
        self.assertNotIn(max_integer([2, 5, 6, 1]), [4, 8, 9])

    def test_Type(self):
        self.assertRaises(TypeError, max_integer("Hola"))
        self.assertRaises(TypeError, max_integer([8, 0, 5.6, 8, 9]))
        self.assertRaises(TypeError, max_integer((3, 6, 8)))

    def test_except(self):
        self.assertRaises(Exception, max_integer, ["Hola", 0, 8, 9])
        self.assertRaises(Exception, max_integer, [8, {4: 6}, '9', (3, 6)])
