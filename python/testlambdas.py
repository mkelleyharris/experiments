#!/usr/bin/python

# Tests of lambda functions in Python
# Goal is learning usage patterns,  and not rigourously testing Python

import unittest

# define some simple lambda functions

add = lambda x,y : x+y
mul = lambda x,y : x*y

# multiple lambda functions with one variable
multiOp = { 'add':lambda x,y : x+y, \
            'mul':lambda x,y : x*y  }

# function that takes a lamba using two variables
def useLambda2( lam, x, y):
  return lam(x, y)


#  Tests follow ----------------------------

class TestLambdas(unittest.TestCase):
  def test_simpleLambdas(self):
    self.assertEqual(5, add(2,3))
    self.assertEqual(8, mul(2,4))

  def test_multiOp(self):
    self.assertEqual(6, multiOp['add'](2,4))
    self.assertEqual(8, multiOp['mul'](2,4))

  def test_function(self):
    self.assertEqual(5, useLambda2(add, 2,3))
    self.assertEqual(6, useLambda2(mul, 2,3))

  def test_listOperations(self):
    self.assertEqual([1, 4, 9, 16], map(lambda x:x**2, [1, 2, 3, 4]))
    list2 = [2,3,4,5]
    cube=lambda x:x**3
    self.assertEqual([8, 27, 64, 125], map(cube, list2))
 
if __name__ == '__main__':
  unittest.main()
