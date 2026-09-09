#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Michael Kelley Harris on 2012-09-15.
Copyright (c) 2012 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import unittest


class untitled:
	def __init__(self):
		pass
		


class untitledTests(unittest.TestCase):
	def setUp(self):
		self.longMessage = True
		pass
		
	def testDemo(self):
		self.assertEqual(1, 3, "Equal check")


if __name__ == '__main__':
	unittest.main()