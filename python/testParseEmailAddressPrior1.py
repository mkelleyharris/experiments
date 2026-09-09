#!/usr/bin/python
"""Tests of calculating CA Tax rates, Married,  in Python. Goal is learning, not testing, Python"""

import unittest

class EmailNameAndAddressFinder:
	
	def __init__(self):
		self.rate = 0

	def getEmailAddress(self, inputText):
		if self.EmailPresent(inputText) == 0:
			return ''
			
		nameAndDomainList = inputText.split("@")
		userName = nameAndDomainList[0]
		emailAddressFrontWords = userNameSide.split(' ')
		userName = emailAddressFrontWords[len(emailAddressFrontWords) -1]
		userName = self.stripOffLeadingBracket(userName)
		
		domain = self.getDomainName(nameAndDomainList)
		return userName + '@' + domain	
		
	def getUserName(self, nameAndDomainList):
		userNameSide = nameAndDomainList[0]
		emailAddressFrontWords = userNameSide.split(' ')
		userName = emailAddressFrontWords[len(emailAddressFrontWords) -1]
		userName = self.stripOffLeadingBracket(userName)
		return userName
		
	def getDomainName(self, nameAndDomainList):
		domainSide = nameAndDomainList[1] 
		emailAddressBackWords = domainSide.split(' ')
		domain = emailAddressBackWords[0]
		domain = self.stripOffTrailingBracket(domain)
		return domain
		
	def stripOffLeadingBracket(self, userName):
		if userName[0] == '(':
			userName = userName.split("(")[1]
			
		if userName[0] == '<':
			userName = userName.split("<")[1]
			
		return userName
		
		
	def stripOffTrailingBracket(self, domain):
		
		if domain[len(domain)-1] == ')':
			domain = domain.split(")")[0]
			
		if domain[len(domain)-1] == '>':
			domain = domain.split(">")[0]
			
		return domain
		
	def EmailPresent(self, inputText):
		stringList = inputText.split("@")
		if len(stringList) == 1:
			return 0

		

class TestEmailNameAndAddressFinder(unittest.TestCase):
	"""Unit tests for EmailNameAndAddressFinder"""

	def test_getEmailAddress_WithNoAddress(self):
		finder = EmailNameAndAddressFinder()		
		self.assertEqual('', finder.getEmailAddress(''))
		self.assertEqual('', finder.getEmailAddress('junk'))
		
	def test_getEmailAddress_WithUnbracketedAddress(self):
		finder = EmailNameAndAddressFinder()		
		self.assertEqual('m@mkh.io', finder.getEmailAddress('Some email m@mkh.io should work.'))
		
	def test_getEmailAddress_WithParenthesis(self):
		finder = EmailNameAndAddressFinder()
		self.assertEqual('m@mkh.io', finder.getEmailAddress('Some email (m@mkh.io) should work.'))
		self.assertEqual('akalman@us.ibm.com', finder.getEmailAddress('Purchased by Alexis Kalman (akalman@us.ibm.com)'))
		
	def test_getEmailAddress_WithGreaterLessThan(self):
		finder = EmailNameAndAddressFinder()		
		self.assertEqual('akalman@us.ibm.com', finder.getEmailAddress('Purchased by Alexis Kalman <akalman@us.ibm.com>'))
		
	#def test_getNameAndEmailAddress(self):
	#	finder = EmailNameAndAddressFinder()		
	#	self.assertEqual('Alexis, Kalman, akalman@us.ibm.com', finder.getEmailAddress('Purchased by Alexis Kalman <akalman@us.ibm.com>'))

if __name__ == '__main__':
    unittest.main()