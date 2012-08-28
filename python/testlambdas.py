#!/usr/bin/python

# Tests of lambda functions in Python

import unittest

# define some simple lambda functions

sum=lambda x,y:x+y

# multiple lambda functions with one variable
ourop = { 'sum':lambda x,y:x+y, \
          'mul':lambda x,y:x*y  }



#  Tests follow ----------------------------

class TestLambdas(unittest.TestCase):
  def test_sum(self):
    self.assertEqual(5, sum(2,3))

  def test_ourop(self):
    self.assertEqual(6, ourop['sum'](2,4))
    self.assertEqual(8, ourop['mul'](2,4))

  def test_listOperations(self):
    self.assertEqual([1, 4, 9, 16], map(lambda x:x**2, [1, 2, 3, 4]))
    list2 = [2,3,4,5]
    cube=lambda x:x**3
    self.assertEqual([8, 27, 64, 125], map(cube, list2))
 
if __name__ == '__main__':
  unittest.main()
