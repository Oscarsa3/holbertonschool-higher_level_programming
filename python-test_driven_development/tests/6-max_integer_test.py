#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Create test of max-integer() function"""

	def test_max(self):
		"""define test"""
		self.assertAlmostEqual(max_integer([3, 5, 8, 9, 2]), 9)
		self.assertAlmostEqual(max_integer([-3, -54678, -2, -456, -22]), -2)
		self.assertAlmostEqual(max_integer([43, -678, 782, 56, -22]), 782)
		self.assertAlmostEqual(max_integer([-3]), -3)
		self.assertAlmostEqual(max_integer([5]), 5)
		self.assertAlmostEqual(max_integer([]), None)
		self.assertAlmostEqual(max_integer(), None)

	def test_values(self):
		"""define test cases"""
		self.assertRaises(TypeError, max_integer("Hola"))
		self.assertRaises(Exception, max_integer((3, 8, 16, 78, 4)))
		self.assertRaises(TypeError, max_integer, [{3: 8}, (4, 7), 9])
