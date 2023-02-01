# Brian Hayes
# 16 Nov 2022

import unittest
import check_functions as mod
from vehicle_mod			import make_vehicle


myAtv1 = make_vehicle(year = "2019", brand = "tao", model = "tao", cc_rating = "110", awd = "no", price = "600", classification = "four wheeler")
myAtv2 = make_vehicle(year = "1997", brand = "honda", model = "fourtrax", cc_rating = "325", awd = "no", price = "870", classification = "four wheeler")
myAtv3 = make_vehicle(year = "2001", brand = "polaris", model = "sportsman", cc_rating = "400", awd = "yes", price = "2100", classification = "four wheeler")
myAtv4 = make_vehicle(year = "2008", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "1600", classification = "four wheeler")
myAtv5 = make_vehicle(year = "2008", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "1100", classification = "four wheeler")

database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5]

class Check_Answer_Tests(unittest.TestCase):
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# check_answer takes a string as a parameter and will return a new string
	# depending on what the parameter is
	#--------------------------------------------------------------------------------------------------#
	
	#TODO - add more tests that will check all the different answers that the funtion
	# now has
	
	# TEST - check_answer is called with a word that appears in the list of
	# affirmative words. Should return "yes"
	def test_check_answer_1(self):
		self.assertEqual("yes", mod.check_answer("yes"))

	# TEST - check_answer is called with a word that appears in the list of
	# words of denial. Should return "no"		
	def test_check_answer_2(self):
		self.assertEqual("no", mod.check_answer("no"))

	# TEST - check_answer is called with a word that cannot be matched
	# should return "other"
	def test_check_answer_3(self):
		self.assertEqual("other", mod.check_answer(""))
		self.assertEqual("other", mod.check_answer(" "))
		self.assertEqual("other", mod.check_answer("1"))
		self.assertEqual("other", mod.check_answer("asduh"))

class Check_Model_Tests(unittest.TestCase):
	

	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# check_model takes a string and a dictionary and will return True or False
	# depending on whether or not that string appears as a value in that dictionary
	#--------------------------------------------------------------------------------------------------#
	
	def test_check_model_1(self):
		self.assertTrue(mod.check_model("fourtrax", database))	
		self.assertFalse(mod.check_model("mymy", database))
		
class Check_Brand_Tests(unittest.TestCase):
	
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# check_brand will take take a string and a database (which is a list of objects) and return True or Fase
	# depending on if the string appears as a brand of any of the objects
	#--------------------------------------------------------------------------------------------------#
	
	def test_check_brand_1(self):
		self.assertTrue(mod.check_brand("honda", database))	
		self.assertFalse(mod.check_brand("mymy", database))
	


class Is_In_Database(unittest.TestCase):
	
	
	def test_is_in_database_1(self): # First in list
		self.assertTrue(mod.is_in_database(myAtv1, database))
		
	def test_is_in_database_2(self): # Second in list
		self.assertTrue(mod.is_in_database(myAtv2, database))
				
	def test_is_in_database_5(self): # Last in list
		self.assertTrue(mod.is_in_database(myAtv5, database))
		
	def test_is_in_database_6(self): # Not in list
		myAtv6 = make_vehicle(year = "2015", brand = "honda", model = "foreman", cc_rating = "400", awd = "yes", price = "1350", classification = "four wheeler")
		self.assertFalse(mod.is_in_database(myAtv6, database))
	


if __name__ == '__main__':
    unittest.main()
