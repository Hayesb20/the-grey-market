# Brian Hayes
# 16 Nov 2022

import unittest
import check_functions as mod
from motor_vehicle_modules import make_atv

model_list = {"yamaha"	: ["banshee", "blaster", "raptor", "yfz", "timberwolf"], 
						"tao" : ["tao"], 
						"polaris" 		: ["explorer", "sportsman", "predator"],
						"kawasaki" 	: ["brute force", "mojave"],
						"honda"		: ["fourtrax", "ex"],
						"suzuki"		:["ltz"]
						}

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
	
	myAtv1 = make_atv("2019", "tao", "tao", "110", "no", "600")
	myAtv2 = make_atv("1997", "honda", "fourtrax", "325", "no", "870")
	myAtv3 = make_atv("2001", "polaris", "sportsman", "400", "yes", "2100")
	myAtv4 = make_atv("2008", "yamaha", "raptor", "600", "no", "1600")
	myAtv5 = make_atv("2008", "yamaha", "raptor", "600", "no", "1100")
	database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5]
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# check_model takes a string and a dictionary and will return True or False
	# depending on whether or not that string appears as a value in that dictionary
	#--------------------------------------------------------------------------------------------------#
	
	def test_check_model_1(self):
		self.assertTrue(mod.check_model("fourtrax", self.database))	
		self.assertFalse(mod.check_model("mymy", self.database))
		
class Check_Brand_Tests(unittest.TestCase):
	
	myAtv1 = make_atv("2019", "tao", "tao", "110", "no", "600")
	myAtv2 = make_atv("1997", "honda", "fourtrax", "325", "no", "870")
	myAtv3 = make_atv("2001", "polaris", "sportsman", "400", "yes", "2100")
	myAtv4 = make_atv("2008", "yamaha", "raptor", "600", "no", "1600")
	myAtv5 = make_atv("2008", "yamaha", "raptor", "600", "no", "1100")
	database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5]
	
	#--------------------------------------------------------------------------------------------------#
	# EXPECTATIONS
	# check_brand will take take a string and a database (which is a list of objects) and return True or Fase
	# depending on if the string appears as a brand of any of the objects
	#--------------------------------------------------------------------------------------------------#
	
	def test_check_brand_1(self):
		self.assertTrue(mod.check_brand("honda", self.database))	
		self.assertFalse(mod.check_brand("mymy", self.database))
	


class Is_In_Database(unittest.TestCase):
	
	myAtv1 = make_atv("2019", "tao", "tao", "110", "no", "600")
	myAtv2 = make_atv("1997", "honda", "fourtrax", "325", "no", "870")
	myAtv3 = make_atv("2001", "polaris", "sportsman", "400", "yes", "2100")
	myAtv4 = make_atv("2008", "yamaha", "raptor", "600", "no", "1600")
	myAtv5 = make_atv("2008", "yamaha", "raptor", "600", "no", "1100")
	database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5]
	
	myAtv6 = make_atv("1996", "kawasaki", "brute", "700", "yes", "4200")
	
	def test_is_in_database_1(self):
		self.assertTrue(mod.is_in_database(self.myAtv1, self.database))
		
	def test_is_in_database_2(self):
		self.assertTrue(mod.is_in_database(self.myAtv2, self.database))
		
	def test_is_in_database_3(self):
		self.assertTrue(mod.is_in_database(self.myAtv3, self.database))
		
	def test_is_in_database_4(self):
		self.assertTrue(mod.is_in_database(self.myAtv4, self.database))
		
	def test_is_in_database_5(self):
		self.assertTrue(mod.is_in_database(self.myAtv5, self.database))
		
	def test_is_in_database_6(self):
		self.assertFalse(mod.is_in_database(self.myAtv6, self.database))
	


if __name__ == '__main__':
    unittest.main()
