#brian hayes
# 17 Nov 2022

import unittest
from atv_class import Atv

import vehicle_mod as mod

class Make_Vehicle_Tests(unittest.TestCase):
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# make_vehicle should create an atv object whos variables are lowercase strings
	# without white spaces, before or after and should fail to create one if any of 
	# the paramiters are empty strings or whitespaces only
	#--------------------------------------------------------------------------------------------------#
	
	# NEED TO DO - make a test that checks what happens when arguments are white spaces
	# NEED TO DO - make a test that when model is given multiple words, the atv is created as 
	#expected (ie: when get_model is called on an atv whos model is big bear should, the
	# returned answer should be "big bear" not "bigbear" )
	
	# TEST make_vehicle is called with all arguments given as they are supposed to be
	def test_for_Make_Vehicle_1(self):
		myAtv = mod.make_vehicle(year = "1998", brand = "yamaha", model = "sport", cc_rating = "35", awd = "yes", price = "2300", classification = "four wheeler")
		self.assertEqual("1998", 		myAtv.get_year())
		self.assertEqual("yamaha",	myAtv.get_brand())
		self.assertEqual("sport", 		myAtv.get_model())
		self.assertEqual("35",				myAtv.get_cc_rating())
		self.assertEqual("yes",			myAtv.get_awd())
		self.assertEqual("2300",			myAtv.get_price())

	# TEST - make_vehicle is called with all arguments given, but arguments contain white spacing.
	def test_for_Make_Vehicle_2(self):
		myAtv = mod.make_vehicle(year = " 19 98 ", brand =  " yam aha ", model = " sp ort ", cc_rating = " 3 5 ", awd = " y es ", price = " 23 00 ", classification = "four wheeler")	
		self.assertEqual("1998", 		myAtv.get_year())
		self.assertEqual("yam aha", 	myAtv.get_brand())
		self.assertEqual("sp ort", 		myAtv.get_model())
		self.assertEqual("35", 			myAtv.get_cc_rating())
		self.assertEqual("yes", 			myAtv.get_awd())
		self.assertEqual("2300",			myAtv.get_price())	
	
	# TEST - make_vehicle is called with all arguments given, but arguments are mixed with upper
	# and lower case chars
	def test_for_Make_Vehicle_3(self):
		myAtv = mod.make_vehicle(year = "2001", brand = "BlaZEr", model = "RaptOr", cc_rating = "35", awd = "YeS", price = "2412", classification = "four wheeler")	
		self.assertEqual("2001", 		myAtv.get_year())
		self.assertEqual("blazer", myAtv.get_brand())
		self.assertEqual("raptor", 		myAtv.get_model())
		self.assertEqual("35", 			myAtv.get_cc_rating())
		self.assertEqual("yes", 		myAtv.get_awd())
		self.assertEqual("2412",		myAtv.get_price())
		
class Confirm_Vehicle_Tests(unittest.TestCase):
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# confirm_atv takes an atv object and returns a string displaying the all different
	# attributes of that atv object
	#--------------------------------------------------------------------------------------------------#
	
	#TEST - confirm_atv is called with an atv whos awd is "yes"
	def test_confirm_vehicle_1(self):
		myAtv = mod.make_vehicle(year = "1998", brand = "yamaha", model = "sport", cc_rating = "35", awd = "yes", price = "2300", classification = "four wheeler")
		message = mod.confirm_vehicle(myAtv)
		self.assertEqual(" 1998 Yamaha Sport 35CC with 4X4 for $2300", message)

	#TEST - confirm_atv is called with an atv whos awd is "no"
	def test_confirm_vehicle_2(self):
		myAtv = mod.make_vehicle(year = "1998", brand = "yamaha", model = "sport", cc_rating = "35", awd = "no", price = "2300", classification = "four wheeler")
		message = mod.confirm_vehicle(myAtv)
		self.assertEqual(" 1998 Yamaha Sport 35CC without 4X4 for $2300", message)




if __name__ == '__main__':
    unittest.main()
		
