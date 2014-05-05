#!/usr/bin/python
"""Tests of lists in Python. Goal is learning, not testing, Python"""

import unittest


class TestLists(unittest.TestCase):
    """Unit tests for basic list features"""

    def test_simple_list(self):
        l_1 = [1]
        l_1.append(2)
        self.assertEqual([1, 2], l_1)

    def test_list_comprehension(self):
        l_1 = [x for x in range(0, 5)]
        self.assertEqual([0, 1, 2, 3, 4], l_1)
        self.assertEqual([1, 4, 9], [x**2 for x in range(1, 4)])

    def test_sort_ascending(self):
        list_orig = [3, 1, 2]
        list_orig.sort()
        self.assertEqual([1, 2, 3], list_orig)

    def test_sort_descending(self):
        list_orig = [3, 1, 2]
        list_orig.sort(reverse=True)
        self.assertEqual([3, 2, 1], list_orig)

    def test_sorted_ascending(self):
        list_orig = [3, 1, 2]
        self.assertEqual([1, 2, 3], sorted(list_orig))

    def test_sorted_descending(self):
        list_orig = [3, 1, 2]
        self.assertEqual([3, 2, 1], sorted(list_orig, reverse=True))



if __name__ == '__main__':
    unittest.main()
