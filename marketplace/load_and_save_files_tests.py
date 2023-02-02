# Brian Hayes
#16 Nov 2022

import unittest
from datetime import datetime
import load_and_save_files as LaS
from atv_class import Atv


newAtv1 = Atv(year = "1997", 
							brand = "yamaha", 
							model = "banshee", 
							cc_rating = "350", 
							awd = "no", 
							price = "3000", 
							classification = "All Terain Vehicle", 
							date = datetime(2020, 5, 17))
newAtv2 = Atv(year = "2020", 
							brand = "polaris", 
							model = "sportsman", 
							cc_rating = "500", 
							awd = "yes", 
							price = "5600", 
							classification = "Four Wheeler", 
							date = datetime(2021, 7, 7))
newAtv3 = Atv(year = "2001", 
							brand = "yamaha", 
							model = "ex", 
							cc_rating = "400", 
							awd = "no", 
							price = "2500", 
							classification = "All Terain Vehicle", 
							date = datetime(2023, 2, 2))
newAtv4 = Atv(year = "2013", 
							brand = "yamaha", 
							model = "kadak", 
							cc_rating = "350", 
							awd = "no", 
							price = "3000", 
							classification = "All Terain Vehicle", 
							date = datetime(2020, 5, 17))

database = [newAtv1, newAtv2, newAtv3, newAtv4]

filename =  "txt_files/test_txts/test_file_1.txt"

class Save_File(unittest.TestCase):
	
	def test_save_file_1(self):
		LaS.save_file(database, filename)
		

class Load_File_Helper(unittest.TestCase):
	
	def test_load_file_helper_1(self):
		empty_database = []
		the_database = LaS.load_file_helper(empty_database, filename)
		for i in range(len(database)):
			self.assertEqual(database[i].get_essence(), the_database[i].get_essence())




if __name__ == '__main__':
    unittest.main()
