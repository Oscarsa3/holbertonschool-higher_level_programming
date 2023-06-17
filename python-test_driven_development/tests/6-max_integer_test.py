#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define test about max_integer() function"""

    def test_max(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)

    def test_igual(self):
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
