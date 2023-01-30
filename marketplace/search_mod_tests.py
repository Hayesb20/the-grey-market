#Brian Hayes
#30 Jan 2023

import unittest
import search_mod as mod

class Is_Valid_Thing_Tests(unittest.TestCase):
	
	def test_is_valid_thing_1(self):
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "polaris"))
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "1998"))
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "sportsman"))
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "400"))
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "no"))
		self.assertTrue(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "1850"))
		self.assertFalse(mod.is_valid_thing(["1998","polaris","sportsman","400","no","1850"], "yamaha"))
		
class Filter_Data_Tests(unittest.TestCase):
	
	def test_filterdata_1(self):
		a_list=["polaris"]
		mod.filter_data(a_list)
		
		
		 













if __name__ == '__main__':
    unittest.main()
