#Brian Hayes
#03 Feb 2023

import sys
sys.path.append("marketplace/class_files")
import unittest
from datetime import datetime
from mower_class import Mower

#Need to add test cases that test the mowers attributes that can be set to default values

# Create a mower object with all possibly parametes filled out
test_mower = Mower (year = "2000", 
					brand = "cub cadet", 
					model = "rzt", 
					hp_rating = "20", 
					cc_rating = "515",
					price = "1500", 
					classification = "zero turn",
					deck_size = "54",
					ist_date = "02 feb 2023",
					engine_brand = "kawasaki")
# Create a mower oject with fewest possible arguments
test_mower2 = Mower ( 
						brand = "cub cadet", 
						model = "rzt", 
						price = "1500", 
						deck_size = "54",)


class Atv_test_case(unittest.TestCase):

	curr_date = datetime.strftime(datetime.now(),"%d %b %Y")
	def test_mower_class_1(self):
		
		# Testing get methods 
		self.assertEqual("515", 		test_mower.get_cc_rating())
		self.assertEqual("20", 			test_mower.get_hp_rating())
		self.assertEqual("2000", 		test_mower.get_year())
		self.assertEqual("cub cadet", 	test_mower.get_brand())
		self.assertEqual("rzt", 		test_mower.get_model())
		self.assertEqual("zero turn", 	test_mower.get_classification())
		self.assertEqual("1500", 		test_mower.get_price())
		self.assertEqual("54", 			test_mower.get_deck_size())
		self.assertEqual(self.curr_date,test_mower.get_list_date())
		self.assertEqual("kawasaki", 	test_mower.get_engine_brand())
		
		self.assertEqual(["zero turn", "cub cadet", "rzt", "54",  "1500", self.curr_date, "515", "20","kawasaki", "2000"], test_mower.get_essence())
	
		self.assertEqual({"classification"	: "zero turn", 	"year" 			: "2000", 
							"brand" 		: "cub cadet", 	"model" 		: "rzt", 
							"deck_size" 	: "54", 		"hp_rating" 	: "20", 
							"price" 		: "1500", 		"list date" 	: self.curr_date,
							"cc_rating" 	: "515", 		"engine_brand" 	: "kawasaki"}, 
							test_mower.get_essence_as_dict())
										
	def test_mower_class_2(self):
	
		# Testing get methods 
		self.assertEqual("unknown",		test_mower2.get_cc_rating())
		self.assertEqual("unknown",		test_mower2.get_hp_rating())
		self.assertEqual("unknown",		test_mower2.get_year())
		self.assertEqual("cub cadet", 	test_mower2.get_brand())
		self.assertEqual("rzt", 		test_mower2.get_model())
		self.assertEqual("mower", 		test_mower2.get_classification())
		self.assertEqual("1500", 		test_mower2.get_price())
		self.assertEqual("54", 			test_mower2.get_deck_size())
		self.assertEqual("unknown", 	test_mower2.get_engine_brand())
		self.assertEqual(self.curr_date,test_mower2.get_list_date())
		
		self.assertEqual(["mower", "cub cadet", "rzt", "54",  "1500", self.curr_date], test_mower2.get_essence())
	
		self.assertEqual({"classification"	: "mower",	"brand" 		: "cub cadet", 	
						"model" 			: "rzt",  	"deck_size" 	: "54", 				 
						"price" 			: "1500", 	"list date" 	: self.curr_date}, 
						test_mower2.get_essence_as_dict())
										
										
if __name__ == '__main__':
    unittest.main()
