#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define test about max_integer() function"""

    def test_max(self):
        """Verificamos si los resultados son precisios o correstos"""
        # Iniciamos los test
        self.assertAlmostEqual(max_integer([-1]), -1)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([3, 3, 3, 3, 3, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 576, -56, -56765]), 576)
        self.assertAlmostEqual(max_integer([-4, -8, -2354, -1]), -1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)

    def test_values(self):
        """Verificamos nuestra funcion"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(Exception, max_integer("Hola"))
        self.assertRaises(Exception, max_integer((3, 6, 8)))
        self.assertRaises(Exception, max_integer, ["Hola", None, 8, 9])
        self.assertRaises(Exception, max_integer, [8, {4: 6}, (3, 6)])
