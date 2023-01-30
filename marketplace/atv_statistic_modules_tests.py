# Brian Hayes
# 14 Nov 2022

import atv_statistic_modules as stat
import unittest

from atv_class import Atv
from working_with_atvs_modules import make_atv

# SET UP STUFF
myAtv1 = make_atv("2019", "tao", "tao", "110", "no", "600")
myAtv2 = make_atv("1997", "honda", "fourtrax", "325", "no", "870")
myAtv3 = make_atv("2001", "polaris", "sportsman", "400", "yes", "2100")
myAtv4 = make_atv("2008", "yamaha", "raptor", "600", "no", "1600")
myAtv5 = make_atv("2008", "yamaha", "raptor", "600", "no", "1100")
myAtv6 = make_atv("2008", "yamaha", "banshee", "600", "no", "1750")
myAtv7 = make_atv("2010", "yamaha", "raptor", "600", "no", "900")
myAtv8 = make_atv("2010", "yamaha", "raptor", "600", "no", "450")
myAtv9 = make_atv("2002", "yamaha", "raptor", "600", "no", "2200")
	
database = [myAtv1, myAtv2, myAtv3, myAtv4, myAtv5,
						myAtv6, myAtv7, myAtv8, myAtv9]

class get_brand_model_year_averages(unittest.TestCase):
	
	def test_see_statistics_1(self):
		myAtv = make_atv("2008", "yamaha", "banshee", "400", "yes", "730")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 1750, list_of_stats["brand, model, year"])
		self.assertEqual( 1750, list_of_stats["brand, model"])
		self.assertEqual( 1333, list_of_stats["brand"])
		
	def test_see_statistics_2(self):
		myAtv = make_atv("2008", "yamaha", "raptor", "400", "yes", "1200")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 1350, list_of_stats["brand, model, year"])
		self.assertEqual( 1250, list_of_stats["brand, model"])
		self.assertEqual( 1333, list_of_stats["brand"])
		
	def test_see_statistics_3(self):
		myAtv = make_atv("2015", "suzuki", "ltz", "400", "yes", "1200")
		list_of_stats = stat.get_brand_model_year_averages(myAtv, database)
		self.assertEqual( 0, list_of_stats["brand, model, year"])
		self.assertEqual( 0, list_of_stats["brand, model"])
		self.assertEqual( 0, list_of_stats["brand"])
		
class Test_get_statistic_message(unittest.TestCase):
	maxDiff = None
	# Testing the less than case
	def test_get_statistic_message_1(self):
		myAtv = make_atv("2008", "yamaha", "banshee", "400", "yes", "730")
		message = stat.get_statistic_message(myAtv, database)		
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $730 is \n $1020 less than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $730 is \n $1020 less than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $730 is \n $603 less than the average price of $1333\n",message)
		
	def test_get_statistic_message_2(self):
		myAtv = make_atv("2008", "yamaha", "banshee", "400", "yes", "1750")
		message = stat.get_statistic_message(myAtv, database)
								
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $1750 is the average price.\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $1750 is the average price.\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $1750 is \n $417 more than the average price of $1333\n",message)
	
	def test_get_statistic_message_3(self):
		myAtv = make_atv("2008", "yamaha", "banshee", "400", "yes", "2000")
		message = stat.get_statistic_message(myAtv, database)								
		self.assertEqual(" Compared to other ATVs that are the same brand, model, "
								+ "and year, \n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $2000 is \n $250 more than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand and model "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $2000 is \n $250 more than the average price of $1750\n"
								+ "\n"
								+ " Compared to other ATVs that are the same brand "
								+ "\n your 2008 Yamaha Banshee 400CC with 4X4 "
								+ "for $2000 is \n $667 more than the average price of $1333\n",message)
		
		
		
		
		
		
		

if __name__ == '__main__':
    unittest.main()




