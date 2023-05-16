#Brian Hayes
# 16 Nov 2022

import sys
sys.path.append("marketplace/modules")

import unittest
import auto_fill_mod as mod
from test_database import atv_data


## BUG: auto_fill() and most_likely() will not function properly if the year is divisable by 25 with a remainder of 0
## and the price is not. Current coding as of 13/Jan/2023 will interpret the numbr divisable by 25 R0 as the price as 
## it is uncomon that prices > 1950 are not produced in incraments of 25 and the other number as the year.





class Autofill_Vehicle_With_ATVs(unittest.TestCase):
	
	# Given a list that appears exactly in atv_data
	def test_autofill_with_atv_1(self):
		user_list = ["1998", "polaris", "xplorer", "400", "yes", "1800"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1998", 	autofilled_dict["year"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual("xplorer", autofilled_dict["model"])
		self.assertEqual("400", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("1800", 	autofilled_dict["price"])
		
	# Given a list that only appears across multiple atv_data entries
	def test_autofill_with_atv_2(self):
		user_list = ["2012", "polaris", "sportsman", "500", "no", "100"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2012", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("100", 		autofilled_dict["price"])
	
############################################################
		                    ## User forgets 1 piece of data for ATV ##
############################################################	
	
	# User does not supply a price
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_3(self):
		user_list = ["2012", "polaris", "sportsman", "500", "no"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2012", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
	# User does not supply the yes/no for awd
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_4(self):
		user_list = ["2012", "polaris", "sportsman", "500", "2800"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2012", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("2800", 		autofilled_dict["price"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
	# User does not supply a year
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_5(self):
		user_list = ["polaris", "sportsman", "500", "no", "1850"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1850", 		autofilled_dict["price"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
	# User does not supply a cc_rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_6(self):
		user_list = ["1998", "polaris", "sportsman",  "no", "1850"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1850", 		autofilled_dict["price"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("1998", 		autofilled_dict["year"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
	# User does not supply a model
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_7(self):
		user_list = ["1998", "polaris", "500", "no", "1850"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1850", 	autofilled_dict["price"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual("1998",	autofilled_dict["year"])
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("no", 		autofilled_dict["awd"])
		self.assertEqual(5, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User does not supply a brand
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_8(self):
		user_list = ["1998", "sportsman", "500", "no", "1850"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1850", 		autofilled_dict["price"])
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("1998",		autofilled_dict["year"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
#############################################################
                                         ## Data appears randomly ##
#############################################################	
	
	# User gives brand, model, awd, year, cc rating, price
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_9(self):
		user_list = ["polaris", "sportsman", "yes", "1998", "500", "1850"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1850", 		autofilled_dict["price"])
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("1998",		autofilled_dict["year"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("yes", 		autofilled_dict["awd"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User gives price, brand, cc_rating, year, model, awd
	# Expectation: autofil will return the unknown price tag as the "price"
	def test_autofill_with_atv_10(self):
		user_list = ["3000", "polaris", "500", "2018", "xplorer","yes"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2018", 	autofilled_dict["year"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual("xplorer",	autofilled_dict["model"])
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("3000",	autofilled_dict["price"])
		self.assertEqual(6, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User gives year, brand, model, cc_rating, price, awd
	# Expectation: autofil will return the unknown price tag as the "price"
	def test_autofill_with_atv_11(self):
		user_list = ["2006", "honda", "foreman", "500", "2800","yes"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2006", 	autofilled_dict["year"])
		self.assertEqual("honda", 	autofilled_dict["brand"])
		#self.assertEqual("foreman",	autofilled_dict["model"])				# Foreman does not appear in the sample dictionar and so it is not present here NEED TO ADDRESS
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("2800",	autofilled_dict["price"])
		self.assertEqual(5, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
############################################################
                           # Data appears randomly and incomplete ##
############################################################	
	
	# User gives brand, model, awd, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_12(self):
		user_list = ["polaris", "sportsman", "yes", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("1998",		autofilled_dict["year"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("yes", 		autofilled_dict["awd"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual(5, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User gives brand,, awd, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_13(self):
		user_list = ["polaris", "yes", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1998",	autofilled_dict["year"])
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(4, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
		# User gives brand, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_14(self):
		user_list = ["polaris", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1998",	autofilled_dict["year"])
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(3, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
		# User gives brand, year
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_15(self):
		user_list = ["polaris", "1998"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("1998", 	autofilled_dict["year"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(2, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	


#############################################################
                           ## User only supplies 1 piece of data ##
#############################################################	
	
	# User gives year
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_16(self):
		user_list = ["2010"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2010", autofilled_dict["year"])
		self.assertEqual(1, 	len(autofilled_dict))
		
	# User gives brand
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_17(self):
		user_list = ["yamaha"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("yamaha", 	autofilled_dict["brand"])
		self.assertEqual(1, 		len(autofilled_dict))		
		
	# User gives model
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_18(self):
		user_list = ["banshee"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("banshee", autofilled_dict["model"])
		self.assertEqual(1, 		len(autofilled_dict))
	
	# User gives only a cc_rating
	# Expectation: will recieve an empty list. a single number means nothing without a brand or model
	def test_autofill_with_atv_19(self):
		user_list = ["400"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual(0,	len(autofilled_dict))			
		
	# User gives awd
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_20(self):
		user_list = ["yes"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("yes", autofilled_dict["awd"])
		self.assertEqual(1, 	len(autofilled_dict))	
		
	# User gives only a price
	# Expectation: autofill will return an empty dictionary. only a number means nothing without a brand or model
	def test_autofill_with_atv_21(self):
		user_list = ["1445"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual({}, autofilled_dict)	
		
	def test_autofill_with_user_input_1(self):
		user_list = ["2001","honda","ex","400","no","2500"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2001", 	autofilled_dict["year"])
		self.assertEqual("honda", 	autofilled_dict["brand"])
		self.assertEqual("ex", 		autofilled_dict["model"])
		self.assertEqual("400", 	autofilled_dict["cc_rating"])
		self.assertEqual("no", 		autofilled_dict["awd"])
		self.assertEqual("2500", 	autofilled_dict["price"])
		self.assertEqual(6, 		len(autofilled_dict))
		
			
#############################################################
         ## Tests that focus of combinations of numbers that are the same ##
#############################################################


	# User supplies a price and cc_rating that are the same number
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_22(self):
		#print("TEST NUMBER 22")
		user_list = ["2000", "polaris", "sportsman", "400", "no","400"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2000", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("400", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above		
		#print("END OF TEST 22")
	# User supplies a price and year that are the same number
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_23(self):
		user_list = ["2000", "polaris", "sportsman", "400", "no","2000"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2000", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400",			autofilled_dict["cc_rating"])
		self.assertEqual("no",			autofilled_dict["awd"])
		self.assertEqual("2000", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	


#################################################################
 ## Tests that focus of combinations of numbers that are within the same ranges ##
#################################################################

	# User supplies a price that is within the acceptable range of years but is not the same number.
	# The price will be divisable by 25 with a R of 0. price will alwasy be given first
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_24(self):
		user_list = ["2000","2014", "polaris", "sportsman", "400", "no"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2014", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("2000", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 6 keys checked above	

	# User supplies a price that is within the acceptable range of cc_rating but is not the same number.
	# The price will be divisable by 25 with a R of 0. price will alwasy be given first, and price will be
	# greater number
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_25(self):
		user_list = ["400","2014", "polaris", "xplorer", "500", "no"]
		autofilled_dict = mod.autofill_vehicle(user_list, atv_data)
		self.assertEqual("2014", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("xplorer",	autofilled_dict["model"])
		self.assertEqual("400", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("500", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 6 keys checked above	
		

	
	

if __name__ == '__main__':
    unittest.main()
