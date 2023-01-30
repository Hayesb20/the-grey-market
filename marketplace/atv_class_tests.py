# Brian Hayes

import unittest
from atv_class import Atv

test_atv = Atv("2000", "yamaha", "Sportsman", "500", "yes", "2500")


class Atv_test_case(unittest.TestCase):
	
	def test_atv_get_attributes(self):
		self.assertEqual("2000", test_atv.get_year())
		self.assertEqual("yamaha", test_atv.get_brand())
		self.assertEqual("Sportsman", test_atv.get_model())
		self.assertEqual("500", test_atv.get_cc_rating())
		self.assertEqual("yes", test_atv.get_awd())
		self.assertEqual("2500", test_atv.get_price())
		

if __name__ == '__main__':
    unittest.main()
		
