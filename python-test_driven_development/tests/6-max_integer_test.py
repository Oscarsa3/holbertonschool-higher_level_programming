#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def lenn(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]))
        self.assertAlmostEqual(max_integer())
