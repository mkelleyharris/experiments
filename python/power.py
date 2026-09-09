#!/usr/bin/python
"""Tests of a simple power function. Non-Recursive & Recursive"""

import unittest


def pow_1(base, exp):
    """Power function. Non-Recursive version"""

    retval = 1
    for i in range(0, exp):
        retval *= base

    return retval


def pow_2(base, exp):
    """Power function. Recursive version"""

    if (exp == 0):
        return 1

    return base * pow_2(base, exp-1)


class TestPow(unittest.TestCase):
    """Unit tests of Power functions, in two forms"""

    def test_pow_1(self):
        self.assertEqual(0, pow_1(0, 1))
        self.assertEqual(3, pow_1(3, 1))
        self.assertEqual(1, pow_1(2, 0))
        self.assertEqual(4, pow_1(2, 2))
        self.assertEqual(8, pow_1(2, 3))


    def test_pow_2(self):
        self.assertEqual(0, pow_2(0, 1))
        self.assertEqual(3, pow_2(3, 1))
        self.assertEqual(1, pow_2(2, 0))
        self.assertEqual(4, pow_2(2, 2))
        self.assertEqual(8, pow_2(2, 3))


if __name__ == '__main__':
    unittest.main()
