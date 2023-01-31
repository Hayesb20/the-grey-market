# Brian Hayes
# 23 Jan 2023


import unittest
import handeling_strings as HS

class Parse(unittest.TestCase):
	
	# Input consists of upper & lower case characterts
	# Exprectation : returns a list of each word with all lowercase characters
	def test_parse_1(self): 
		string = "2009 Polaris Sportsman 350 no 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		a_list = HS.parse(string)
		self.assertEqual(expected_list, HS.parse(string))
		
	# Input consists of all upper case characterts
	# Exprectation : returns a list of each word with all lowercase characters
	def test_parse_2(self): 
		string = "2009 POLARIS SPORTSMAN 350 NO 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		a_list = HS.parse(string)
		self.assertEqual(expected_list, HS.parse(string))
		
	# Input consists of all lower case characterts
	# Exprectation : returns a list of each word with all lowercase characters
	def test_parse_3(self): 
		string = "2009 polaris sportsman 350 no 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		a_list = HS.parse(string)
		self.assertEqual(expected_list, HS.parse(string))
		
		
		
		
		
if __name__ == '__main__':
    unittest.main()
	
