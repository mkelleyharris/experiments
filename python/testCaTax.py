#!/usr/bin/python
"""Tests of calculating CA Tax rates, Married,  in Python. Goal is learning, not testing, Python"""

import unittest

class CaTax:
	
	def __init__(self):
		self.rate = 0
		
	def getTaxRate(self, income):
		if (income < 16030.00):
			return 0.01
			
		if (income < 38003.00):
			return 0.02
			
		else:
			return 0.04
			
	def getTax(self, income):
		return income * self.getTaxRate(income);
		

class TestCaTaxRate(unittest.TestCase):
    """Unit tests for CA tax rates"""

    def test_getTaxRate(self):
		tax = CaTax()
		self.assertEqual(0.01, tax.getTaxRate(0))
		self.assertEqual(0.01, tax.getTaxRate(16029.99))
		self.assertEqual(0.02, tax.getTaxRate(16030.00))
		self.assertEqual(0.04, tax.getTaxRate(38003.00))
		
    def test_getTax(self):
		tax = CaTax()
		self.assertEqual(0, tax.getTax(0))
		self.assertEqual(0.01*1000, tax.getTax(1000.00))
		self.assertEqual(0.02*16030, tax.getTax(16030.00))

if __name__ == '__main__':
    unittest.main()