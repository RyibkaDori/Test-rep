import unittest

from numpy.ma.core import equal


def quick_sort(arr):
    if not isinstance(arr, list):
        raise TypeError("Argument is not a list")
    if len(arr) <= 1:
        return arr
    if len(arr) == 1:
        return arr
    pivot = arr[-1]
    left = []
    equals = []
    right = []
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        elif num == pivot:
            equals.append(num)
    return quick_sort(left) + equals + quick_sort(right)

class TestTypesOfVariables(unittest.TestCase):
    def test_quick_sort(self):
        self.assertRaises(TypeError, quick_sort, None)
        self.assertRaises(TypeError, quick_sort, {})
        self.assertRaises(TypeError, quick_sort, 'l')
        self.assertRaises(TypeError, quick_sort, 1)
class TestEmptyList(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([]),[],"should be empty")
class TestListOfIncorrectArgs(unittest.TestCase):
    def test_quick_sort(self):
        with self.assertRaises(TypeError):
            quick_sort([1, "2", 3, "4"])
            quick_sort([1, [1], 2])
            quick_sort([1, (1,2), 1])
class TestAccuracyOfWorking(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([1, 2]), [1, 2], "should be [1,2]")
        self.assertEqual(quick_sort([2]), [2], "should be [2]")
        self.assertEqual(quick_sort([23,2,45,65666,7]), [2, 7, 23, 45, 65666], "should be [2,7,23,45,65666]")
class TestEqualArgs(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort([1, 1, 1, 1]), [1, 1, 1, 1], "should be [1, 1, 1, 1]")
