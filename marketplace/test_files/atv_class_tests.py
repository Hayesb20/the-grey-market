# Brian Hayes

import unittest
from test_database import t_atv1

class Atv_test_case(unittest.TestCase):
	
	def t_atv_get_attributes(self):
		self.assertEqual("500", t_atv1.get_cc_rating())
		self.assertEqual("2000", t_atv1.get_year())
		self.assertEqual("yamaha", t_atv1.get_brand())
		self.assertEqual("sportsman", t_atv1.get_model())
		self.assertEqual("four wheeler", t_atv1.get_classification())
		self.assertEqual("yes", t_atv1.get_awd())
		self.assertEqual("2500", t_atv1.get_price())
		
	def t_atv_get_essence(self):
		self.assertEqual(["four wheeler", "2000", "yamaha", "sportsman", "500", "yes", "2500", "02 Feb 2023"], t_atv1.get_essence())
	
	def test_get_essence_as_dict(self):
		self.assertEqual({"classification" : "four wheeler", 
							"year" : "2000", 
							"brand" : "yamaha", 
							"model" : "sportsman", 
							"cc_rating" : "500", 
							"awd" : "yes", 
							"price" : "2500",
							"list date" : "02 Feb 2023"}, t_atv1.get_essence_as_dict())
		
















if __name__ == '__main__':
    unittest.main()
		
