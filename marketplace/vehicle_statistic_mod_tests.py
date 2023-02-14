# Brian Hayes
# 14 Nov 2022

import unittest
import vehicle_statistic_mod as stat

from atv_class import Atv
from vehicle_mod import make_vehicle

# SET UP STUFF
myAtv1 = make_vehicle(year = "2019", brand = "tao", model = "tao", cc_rating = "110", awd = "no", price = "600", classification = "four wheeler")
myAtv2 = make_vehicle(year = "1997", brand = "honda", model = "fourtrax", cc_rating = "325", awd = "no", price = "870", classification = "four wheeler")
myAtv3 = make_vehicle(year = "2001", brand = "polaris", model = "sportsman", cc_rating = "400", awd = "yes", price = "2100", classification = "four wheeler")
myAtv4 = make_vehicle(year = "2008", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "1600", classification = "four wheeler")
myAtv5 = make_vehicle(year = "2008", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "1100", classification = "four wheeler")
myAtv6 = make_vehicle(year = "2008", brand = "yamaha", model = "banshee", cc_rating = "600", awd = "no", price = "1750", classification = "four wheeler")
myAtv7 = make_vehicle(year = "2010", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "900", classification = "four wheeler")
myAtv8 = make_vehicle(year = "2010", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "450", classification = "four wheeler")
myAtv9 = make_vehicle(year = "2002", brand = "yamaha", model = "raptor", cc_rating = "600", awd = "no", price = "2200", classification = "four wheeler")
	
database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5,
						myAtv6, myAtv7, myAtv8, myAtv9]

class get_brand_model_year_averages(unittest.TestCase):
	
	def test_see_statistics_1(self):
		myAtv = make_vehicle(year = "2008", brand = "yamaha", model = "banshee", cc_rating = "400", awd = "yes", price = "730", classification = "four wheeler")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 1750, list_of_stats["brand, model, year"])
		self.assertEqual( 1750, list_of_stats["brand, model"])
		self.assertEqual( 1333, list_of_stats["brand"])
		
	def test_see_statistics_2(self):
		myAtv = make_vehicle(year = "2008", brand = "yamaha", model = "raptor", cc_rating = "400", awd = "yes", price = "1200", classification = "four wheeler")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 1350, list_of_stats["brand, model, year"])
		self.assertEqual( 1250, list_of_stats["brand, model"])
		self.assertEqual( 1333, list_of_stats["brand"])
		
	def test_see_statistics_3(self):
		myAtv = make_vehicle(year = "2015", brand = "suzuki", model = "ltz", cc_rating = "400", awd = "yes", price = "1200", classification = "four wheeler")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 0, list_of_stats["brand, model, year"])
		self.assertEqual( 0, list_of_stats["brand, model"])
		self.assertEqual( 0, list_of_stats["brand"])
		
class Test_get_statistic_message(unittest.TestCase):
	maxDiff = None
	# Testing the less than case
	def test_get_statistic_message_1(self):
		myAtv = make_vehicle(year = "2008", brand = "yamaha", model = "banshee", cc_rating = "400", awd = "yes", price = "730", classification = "four wheeler")
		message = stat.get_statistic_message(myAtv, database)		
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $730 is \n $1020 less than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $730 is \n $1020 less than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $730 is \n $603 less than the average price of $1333\n",message)
		
	def test_get_statistic_message_2(self):
		myAtv = make_vehicle(year = "2008", brand = "yamaha", model = "banshee", cc_rating = "400", awd = "yes", price = "1750", classification = "four wheeler")
		message = stat.get_statistic_message(myAtv, database)
								
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $1750 is the average price.\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $1750 is the average price.\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $1750 is \n $417 more than the average price of $1333\n",message)
	
	def test_get_statistic_message_3(self):
		myAtv = make_vehicle(year = "2008", brand = "yamaha", model = "banshee", cc_rating = "400", awd = "yes", price = "2000", classification = "four wheeler")
		message = stat.get_statistic_message(myAtv, database)								
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $2000 is \n $250 more than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $2000 is \n $250 more than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee with a 400CC Engine, with 4X4 "
								+ "for $2000 is \n $667 more than the average price of $1333\n",message)
		
		
		
		
		
		
		

if __name__ == '__main__':
    unittest.main()




