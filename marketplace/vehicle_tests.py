#brian hayes
# 17 Nov 2022

import unittest
from atv_class import Atv

import working_with_atvs_modules as mod

class Make_Atv_Tests(unittest.TestCase):
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# make_atv should create an atv object whos variables are lowercase strings
	# without white spaces, before or after and should fail to create one if any of 
	# the paramiters are empty strings or whitespaces only
	#--------------------------------------------------------------------------------------------------#
	
	# NEED TO DO - make a test that checks what happens when arguments are white spaces
	# NEED TO DO - make a test that when model is given multiple words, the atv is created as 
	#expected (ie: when get_model is called on an atv whos model is big bear should, the
	# returned answer should be "big bear" not "bigbear" )
	
	# TEST make_atv is called with all arguments given as they are supposed to be
	def test_for_Make_Atv_1(self):
		myAtv = mod.make_atv("1998", "yamaha", "sport", "35", "yes", "2300")
		self.assertEqual("1998", 		myAtv.get_year())
		self.assertEqual("yamaha", myAtv.get_brand())
		self.assertEqual("sport", 		myAtv.get_model())
		self.assertEqual("35",			myAtv.get_cc_rating())
		self.assertEqual("yes",		myAtv.get_awd())
		self.assertEqual("2300",		myAtv.get_price())

	# TEST - make_atv is called with all arguments given, but arguments contain white spacing.
	def test_for_Make_Atv_2(self):
		myAtv = mod.make_atv(" 19 98 ", " yam aha ", " sp ort ", " 3 5 ", " y es ", " 23 00 ")	
		self.assertEqual("1998", 		myAtv.get_year())
		self.assertEqual("yam aha", myAtv.get_brand())
		self.assertEqual("sp ort", 		myAtv.get_model())
		self.assertEqual("35", 			myAtv.get_cc_rating())
		self.assertEqual("yes", 		myAtv.get_awd())
		self.assertEqual("2300",		myAtv.get_price())	
	
	# TEST - make_atv is called with all arguments given, but arguments are mixed with upper
	# and lower case chars
	def test_for_Make_Atv_3(self):
		myAtv = mod.make_atv("2001", "BlaZEr", "RaptOr", "35", "YeS", "2412")	
		self.assertEqual("2001", 		myAtv.get_year())
		self.assertEqual("blazer", myAtv.get_brand())
		self.assertEqual("raptor", 		myAtv.get_model())
		self.assertEqual("35", 			myAtv.get_cc_rating())
		self.assertEqual("yes", 		myAtv.get_awd())
		self.assertEqual("2412",		myAtv.get_price())
		
class Confirm_Atv_Tests(unittest.TestCase):
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# confirm_atv takes an atv object and returns a string displaying the all different
	# attributes of that atv object
	#--------------------------------------------------------------------------------------------------#
	
	#TEST - confirm_atv is called with an atv whos awd is "yes"
	def test_confirm_atv_1(self):
		myAtv = mod.make_atv("1998", "yamaha", "sport", "35", "yes", "2300")
		message = mod.confirm_atv(myAtv)
		self.assertEqual(" 1998 Yamaha Sport 35CC with 4X4 for $2300", message)

	#TEST - confirm_atv is called with an atv whos awd is "no"
	def test_confirm_atv_2(self):
		myAtv = mod.make_atv("1998", "yamaha", "sport", "35", "no", "2300")
		message = mod.confirm_atv(myAtv)
		self.assertEqual(" 1998 Yamaha Sport 35CC without 4X4 for $2300", message)




if __name__ == '__main__':
    unittest.main()
		
