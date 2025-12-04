import unittest

import numpy as np

from MNK import least_squares
class TestTypesOfVariables(unittest.TestCase):
    def test_least_squares(self):
        self.assertRaises(TypeError, least_squares, None)
        self.assertRaises(TypeError, least_squares, ())
        self.assertRaises(TypeError, least_squares, {})
        self.assertRaises(TypeError, least_squares, 'l')
class TestListOfZeros(unittest.TestCase):
    def test_least_squares(self):
        self.assertEqual(least_squares(np.array([0,0,0]),np.array([1,1,1])), 'Zero cant be a divider', "should be 'Zero cant be a divider'")
class TestListOfStrings(unittest.TestCase):
    def test_least_squares(self):
        self.assertEqual(least_squares(np.array(['str', 0, 0]), np.array([1, 1, 1])), 'Your list is non-numeric',
                         "should be 'Your list is non-numeric'")



if __name__ == '__main__':
    unittest.main()