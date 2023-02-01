# Brian Hayes

import unittest
from atv_class import Atv
from vehicle_class import Vehicle


test_atv = Atv(year = "2000", 
							brand = "yamaha", 
							model = "sportsman", 
							cc_rating = "500", 
							awd = "yes", 
							price = "2500", 
							classification = "four wheeler")


class Atv_test_case(unittest.TestCase):
	
	def test_atv_get_attributes(self):
		self.assertEqual("500", test_atv.get_cc_rating())
		self.assertEqual("2000", test_atv.get_year())
		self.assertEqual("yamaha", test_atv.get_brand())
		self.assertEqual("sportsman", test_atv.get_model())
		self.assertEqual("four wheeler", test_atv.get_classification())
		self.assertEqual("yes", test_atv.get_awd())
		self.assertEqual("2500", test_atv.get_price())
		
	def test_atv_get_essence(self):
		self.assertEqual(["four wheeler", "2000", "yamaha", "sportsman", "500", "yes", "2500"], test_atv.get_essence())
	
	def test_get_essence_as_dict(self):
		self.assertEqual({"classification" : "four wheeler", 
										"year" : "2000", 
										"brand" : "yamaha", 
										"model" : "sportsman", 
										"cc_rating" : "500", 
										"awd" : "yes", 
										"price" : "2500"}, test_atv.get_essence_as_dict())
		
















if __name__ == '__main__':
    unittest.main()
		
