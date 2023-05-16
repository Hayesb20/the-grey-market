# Brian Hayes
# 11 Apr 2023

import sys
sys.path.append("marketplace/class_files")
sys.path.append("marketplace/modules")


import unittest
import auto_fill_mod as mod
from test_database import mower_data


class Find_Engine_Brand(unittest.TestCase):
	def test_feb1 (self):
		# Need to make sure that will find briggs and stratton
		users_list = ["briggs and stratton"]
		self.assertEqual("briggs and stratton", mod.find_engine_brand(users_list))
		users_list = ["briggs & stratton"]
		self.assertEqual("briggs & stratton", mod.find_engine_brand(users_list))
		users_list = ["briggs"]
		self.assertEqual("briggs", mod.find_engine_brand(users_list))

class Autofill_Vehicle_With_Mowers(unittest.TestCase):
	
	def est_autofill_with_mower_1(self):
		user_list = ["2012", "snapper", "yx42", "22", "550", "riding mower", "54","kawasaki"]
		autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
		#print(autofilled_dict)
		self.assertEqual("snapper", autofilled_dict["brand"])
		self.assertEqual("yx42",    autofilled_dict["model"])
		self.assertEqual("2012",    autofilled_dict["year"])
		self.assertEqual("22",      autofilled_dict["hp_rating"])
		self.assertEqual("550",     autofilled_dict["price"])
		self.assertEqual("54",      autofilled_dict["deck_size"])
		self.assertEqual("kawasaki", autofilled_dict["engine_brand"])

	def test_autofill_with_mower_2 (self):
		user_list = ["exmark", "lazer z", "kohler", "2700", "60"]
		autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
		#print(autofilled_dict)
		self.assertEqual("exmark",  autofilled_dict["brand"])
		self.assertEqual("lazer z", autofilled_dict["model"])
		self.assertEqual("kohler",  autofilled_dict["engine_brand"])
		self.assertEqual("2700",    autofilled_dict["price"])
		self.assertEqual("60",      autofilled_dict["deck_size"])
	
	# Testing autofill with a mower whos information must be collected from
	# multiple mowers found in the database
	def est_autofill_with_a_mower1(self):
		user_list = ["snapper", "lt1940", "22", "50", "1950"]
		autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
		#print(autofilled_dict)
		self.assertEqual("snapper", autofilled_dict["brand"])
		self.assertEqual("lt1940", 	autofilled_dict["model"])
		self.assertEqual("22",  	autofilled_dict["hp_rating"])
		self.assertEqual("1950",    autofilled_dict["price"])
		self.assertEqual("50",      autofilled_dict["deck_size"])

	# Tests autofill with a mower that has no relationship to anything in the database
	def est_autofill_with_a_mower2(self):
		# Autofill as no way to infer any of the below information if the brand
		# and model cannot be found in the database
		user_list = ["yardman", "mtd", "12.5", "38", "435", "briggs and stratton"]
		autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
		#print(autofilled_dict)
		#self.assertEqual("yardman", 			autofilled_dict["brand"])
		#self.assertEqual("mtd", 				autofilled_dict["model"])
		#self.assertEqual("12.5",  				autofilled_dict["hp_rating"])
		#self.assertEqual("435",    				autofilled_dict["price"])
		#self.assertEqual("38",      			autofilled_dict["deck_size"])
		self.assertEqual("briggs and stratton",	autofilled_dict["engine_brand"])

	




if __name__ == '__main__':
    unittest.main()