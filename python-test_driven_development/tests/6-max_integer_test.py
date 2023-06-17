#!/usr/bin/python3
"""Unittest for max_integer([..])"
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define test about max_integer() function"""

    def test_max(self):
        """Verificamos si los resultados son precisios o correstos"""

        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 576, -56, -5678898765]), 576)
        self.assertAlmostEqual(max_integer([-4, -8, -2354, -1]), -1)
        self.assertAlmostEqual(max_integer([23, 65, 789]), 789)
        self.assertAlmostEqual(max_integer([0, 4565, 34, 5, 876]), 4565)
        self.assertAlmostEqual(max_integer([]), None)

    def test_none(self):
        """Verificamos cuando nuestra funcion está vacía"""
        self.assertIsNone(max_integer())

    def test_except(self):
        """Verificamos nuestra funcion enviando diferentes
        tipos de datos y tambien dentro de una lista"""

        self.assertRaises(Exception, max_integer("Hola"))
        self.assertRaises(Exception, max_integer('8'))
        self.assertRaises(Exception, max_integer((3, 6, 8)))
        self.assertRaises(Exception, max_integer, ["Hola", 0, 8, 9])
        self.assertRaises(Exception, max_integer, [8, {4: 6}, '9', (3, 6)])
