#!/usr/bin/python

# Tests of lists in Python
# Goal is learning usage patterns,  and not rigourously testing Python

import unittest



#  Tests follow ----------------------------

class TestLists(unittest.TestCase):
  def test_simpleList(self):
    l1 = [1]
    l1.append(2)
    self.assertEqual([1, 2], l1)

  def test_listComprehension1(self):
    l1 = [ x for x in range(0, 5)]
    self.assertEqual([0, 1, 2, 3, 4], l1)
    self.assertEqual([1, 4, 9], [x**2 for x in range(1,4)])

  def test_sortAscending(self):
	listOrig = [3, 1, 2]
	listOrig.sort()
	self.assertEqual([1, 2, 3], listOrig)
	
  def test_sortDescending(self):
	listOrig = [3, 1, 2]
	listOrig.sort(reverse=True)
	self.assertEqual([3, 2, 1], listOrig)
	
  def test_sortedAscending(self):
	listOrig = [3, 1, 2]
	self.assertEqual([1, 2, 3], sorted(listOrig))
	
  def test_sortedDescending(self):
	listOrig = [3, 1, 2]
	self.assertEqual([3, 2, 1], sorted(listOrig, reverse=True))

 
if __name__ == '__main__':
  unittest.main()
