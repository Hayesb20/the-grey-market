#Brian Hayes
#01 Feb 2023

import unittest
from item_class import Item
from datetime import datetime

class Item_test(unittest.TestCase):
	
	def test_item_get_methods1(self):
		my_item = Item(brand = "yamaha", price = "3000")
		self.assertEqual("yamaha", my_item.get_brand())
		self.assertEqual("3000", my_item.get_price())
		self.assertEqual(datetime.now().strftime("%d %b %Y"), my_item.get_list_date())
		
	def test_item_get_methods2(self):
		my_item = Item(brand = "brazil", price = "3", list_date = "17 may 2020")
		self.assertEqual("brazil", my_item.get_brand())
		self.assertEqual("3", my_item.get_price())
		self.assertEqual("17 May 2020", my_item.get_list_date())



if __name__ == '__main__':
    unittest.main()
