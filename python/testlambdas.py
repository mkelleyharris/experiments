#!/usr/bin/python
"""Tests of lambda functions, for learning, not testing, Python"""
# Note Lamda's are a bit controversial. Simple functions are often clearer.

import unittest

# define some simple lambda functions

ADDIT = lambda x, y: x+y
MULT = lambda x, y: x*y

# multiple lambda functions with one variable
MULTI_OP = {'ADDIT':lambda x, y: x+y, \
            'MULT':lambda x, y: x*y}

# function that takes a lamba using two variables
def use_lambda_2(lam, x, y):
    return lam(x, y)


#  Tests follow ----------------------------

class TestLambdas(unittest.TestCase):
    """Unit tests for Lambda's"""

    def test_simple_lambdas(self):
        self.assertEqual(5, ADDIT(2, 3))
        self.assertEqual(8, MULT(2, 4))

    def test_multi_op(self):
        self.assertEqual(6, MULTI_OP['ADDIT'](2, 4))
        self.assertEqual(8, MULTI_OP['MULT'](2, 4))

    def test_function(self):
        self.assertEqual(5, use_lambda_2(ADDIT, 2, 3))
        self.assertEqual(6, use_lambda_2(MULT, 2, 3))

    def test_list_operations(self):
        self.assertEqual([1, 4, 9, 16], map(lambda x: x**2, [1, 2, 3, 4]))
        list2 = [2, 3, 4, 5]
        cube = lambda x: x**3
        self.assertEqual([8, 27, 64, 125], map(cube, list2))


if __name__ == '__main__':
    unittest.main()
