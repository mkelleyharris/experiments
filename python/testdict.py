#!/usr/bin/python
"""Tests of dictionaries in Python. Goal is learning, not testing, Python"""

import unittest


class TestDicts(unittest.TestCase):
    """Unit tests for basic dictionary features"""

    def test_add(self):
        d = {}
        d['a'] = 4
        self.assertEqual({'a': 4}, d)
        self.assertEqual(4, d['a'])

    def test_initialize_and_get(self):
        d = {'a': 1, 'b':2, 'c':3}
        self.assertEqual(1, d['a'])
        self.assertEqual(2, d['b'])
        self.assertEqual(3, d['c'])

    def test_modify_in_place(self):
        d = {'a': 1, 'b':2, 'c':3}
        self.assertEqual(1, d['a'])
        d['a'] = 7
        self.assertEqual(7, d['a'])
        self.assertEqual({'a': 7, 'b':2, 'c':3}, d)


if __name__ == '__main__':
    unittest.main()
