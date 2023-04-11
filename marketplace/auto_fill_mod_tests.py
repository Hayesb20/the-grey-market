#Brian Hayes
# 16 Nov 2022

import unittest
#import auto_fill_mod as mod
import auto_fill_mod as mod
from atv_class import Atv
from mower_class import Mower


## BUG: auto_fill() and most_likely() will not function properly if the year is divisable by 25 with a remainder of 0
## and the price is not. Current coding as of 13/Jan/2023 will interpret the numbr divisable by 25 R0 as the price as 
## it is uncomon that prices > 1950 are not produced in incraments of 25 and the other number as the year.

test_atv1 = 	Atv(year = "1997", brand = "yamaha", 	model = "banshee", 		cc_rating = "350", 	awd = "no", 	price = "3000", 	classification = "four wheeler")
test_atv2 = 	Atv(year = "2015", brand = "kawasaki", 	model = "brute force", 	cc_rating = "750", 	awd = "yes", 	price = "4250", 	classification = "four wheeler")
test_atv3 = 	Atv(year = "2012", brand = "polaris", 	model = "sportsman", 	cc_rating = "400", 	awd = "yes", 	price = "400", 		classification = "four wheeler")
test_atv4 = 	Atv(year = "2002", brand = "polaris", 	model = "sportsman", 	cc_rating = "500", 	awd = "yes", 	price = "2800", 	classification = "four wheeler")
test_atv5 = 	Atv(year = "1998", brand = "polaris", 	model = "xplorer", 		cc_rating = "400", 	awd = "yes", 	price = "1800", 	classification = "four wheeler")
test_atv6 = 	Atv(year = "1987", brand = "honda", 	model = "fourtrax", 	cc_rating = "350", 	awd = "yes", 	price = "600", 		classification = "four wheeler")
test_atv7 = 	Atv(year = "1996", brand = "polaris", 	model = "sportsman", 	cc_rating = "350", 	awd = "no", 	price = "100", 		classification = "four wheeler")
test_atv8 = 	Atv(year = "2000", brand = "polaris", 	model = "sportsman", 	cc_rating = "1000", awd = "no", 	price = "2000", 	classification = "four wheeler")
test_atv9 = 	Atv(year = "2022", brand = "polaris", 	model = "sportsman", 	cc_rating = "500", 	awd = "yes", 	price = "1350", 	classification = "four wheeler")
test_atv10 = 	Atv(year = "2018", brand = "polaris", 	model = "xplorer", 		cc_rating = "400", 	awd = "yes", 	price = "1600", 	classification = "four wheeler")
test_atv11 = 	Atv(year = "2009", brand = "honda", 	model = "fourtrax", 	cc_rating = "350", 	awd = "yes", 	price = "600", 		classification = "four wheeler")
test_atv12 = 	Atv(year = "2004", brand = "polaris", 	model = "sportsman", 	cc_rating = "350", 	awd = "no", 	price = "400", 		classification = "four wheeler")
test_atv13 = 	Atv(year = "2012", brand = "polaris", 	model = "sportsman", 	cc_rating = "1000", awd = "no", 	price = "450", 		classification = "four wheeler")
test_atv14 = 	Atv(year = "2012", brand = "honda", 	model = "ex", 			cc_rating = "400", 	awd = "no", 	price = "2500", 	classification = "four wheeler")
test_mower1 = 	Mower(year="2012", brand = "snapper", 	model="yx42", 	hp_rating="22", cc_rating="560", price="550", classification="riding mower", deck_size="54", list_date="02 feb 2023", engine_brand="kawasaki")
	
the_data = [test_atv1, test_atv2, test_atv3, test_atv4, test_atv5, test_atv6, test_atv7,
			test_atv8,test_atv9, test_atv10, test_atv11, test_atv12, test_atv13, test_atv14,
			test_mower1]

class Autofill_Vehicle_With_Mowers(unittest.TestCase):
	def est_autofill_with_mower_1(self):
		user_list = ["2012", "snapper", "yx42", "22", "560", "550", "riding mower", "54", "02 feb 2023"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		print(autofilled_dict)


class Autofill_Vehicle_With_ATVs(unittest.TestCase):
	
	# Given a list that appears exactly in the_data
	def test_autofill_with_atv_1(self):
		user_list = ["1998", "polaris", "xplorer", "400", "yes", "1800"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("1998", 	autofilled_dict["year"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual("xplorer", autofilled_dict["model"])
		self.assertEqual("400", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("1800", 	autofilled_dict["price"])
		
	# Given a list that only appears across multiple the_data entries
	def test_autofill_with_atv_2(self):
		user_list = ["2012", "polaris", "sportsman", "500", "no", "100"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("1850", 			autofilled_dict["price"])
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("1998",				autofilled_dict["year"])
		self.assertEqual("500", 				autofilled_dict["cc_rating"])
		self.assertEqual("yes", 				autofilled_dict["awd"])
		self.assertEqual("polaris", 		autofilled_dict["brand"])
		self.assertEqual(6, 						len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User gives price, brand, cc_rating, year, model, awd
	# Expectation: autofil will return the unknown price tag as the "price"
	def test_autofill_with_atv_10(self):
		user_list = ["3000", "polaris", "500", "2018", "xplorer","yes"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2006", 	autofilled_dict["year"])
		self.assertEqual("honda", 	autofilled_dict["brand"])
		#self.assertEqual("foreman",	autofilled_dict["model"])				# Foreman does not appear in the sample dictionar and so it is not present here NEED TO ADDRESS
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual("2800",	autofilled_dict["price"])
		self.assertEqual(5, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
#############################################################
                           ## Data appears randomly and incomplete ##
#############################################################	
	
	# User gives brand, model, awd, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_12(self):
		user_list = ["polaris", "sportsman", "yes", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("sportsman", 	autofilled_dict["model"])
		self.assertEqual("1998",				autofilled_dict["year"])
		self.assertEqual("500", 				autofilled_dict["cc_rating"])
		self.assertEqual("yes", 				autofilled_dict["awd"])
		self.assertEqual("polaris", 		autofilled_dict["brand"])
		self.assertEqual(5, 						len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
	# User gives brand,, awd, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_13(self):
		user_list = ["polaris", "yes", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("1998",		autofilled_dict["year"])
		self.assertEqual("500", 		autofilled_dict["cc_rating"])
		self.assertEqual("yes", 		autofilled_dict["awd"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(4, 				len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	
	
		# User gives brand, year, cc rating
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_14(self):
		user_list = ["polaris", "1998", "500"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("1998",	autofilled_dict["year"])
		self.assertEqual("500", 	autofilled_dict["cc_rating"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(3, 		len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above
	
		# User gives brand, year
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_15(self):
		user_list = ["polaris", "1998"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("1998", 	autofilled_dict["year"])
		self.assertEqual("polaris", autofilled_dict["brand"])
		self.assertEqual(2, 				len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	


#############################################################
                           ## User only supplies 1 piece of data ##
#############################################################	
	
	# User gives year
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_16(self):
		user_list = ["2010"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2010", autofilled_dict["year"])
		self.assertEqual(1, 			len(autofilled_dict))
		
	# User gives brand
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_17(self):
		user_list = ["yamaha"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("yamaha", autofilled_dict["brand"])
		self.assertEqual(1, 				 len(autofilled_dict))		
		
	# User gives model
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_18(self):
		user_list = ["banshee"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("banshee", autofilled_dict["model"])
		self.assertEqual(1, 		len(autofilled_dict))
	
	# User gives only a cc_rating
	# Expectation: will recieve an empty list. a single number means nothing without a brand or model
	def test_autofill_with_atv_19(self):
		user_list = ["400"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual(0,	len(autofilled_dict))			
		
	# User gives awd
	# Expectation: autofill will appropreatly fill all known data without error
	def test_autofill_with_atv_20(self):
		user_list = ["yes"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("yes", 	autofilled_dict["awd"])
		self.assertEqual(1, 			len(autofilled_dict))	
		
	# User gives only a price
	# Expectation: autofill will return an empty dictionary. only a number means nothing without a brand or model
	def test_autofill_with_atv_21(self):
		user_list = ["1445"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual({}, autofilled_dict)	
		
	def test_autofill_with_user_input_1(self):
		user_list = ["2001","honda","ex","400","no","2500"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2001", autofilled_dict["year"])
		self.assertEqual("honda", autofilled_dict["brand"])
		self.assertEqual("ex", autofilled_dict["model"])
		self.assertEqual("400", autofilled_dict["cc_rating"])
		self.assertEqual("no", autofilled_dict["awd"])
		self.assertEqual("2500", autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict))
		
			
#############################################################
         ## Tests that focus of combinations of numbers that are the same ##
#############################################################


	# User supplies a price and cc_rating that are the same number
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_22(self):
		user_list = ["2000", "polaris", "sportsman", "400", "no","400"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2000", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("400", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above		
	
	# User supplies a price and year that are the same number
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_23(self):
		user_list = ["2000", "polaris", "sportsman", "400", "no","2000"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2000", 			autofilled_dict["year"])
		self.assertEqual("polaris", 		autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400", 				autofilled_dict["cc_rating"])
		self.assertEqual("no", 				autofilled_dict["awd"])
		self.assertEqual("2000", 			autofilled_dict["price"])
		self.assertEqual(6, 						len(autofilled_dict)) # Assure that the dict only has the 5 keys checked above	


#################################################################
 ## Tests that focus of combinations of numbers that are within the same ranges ##
#################################################################

	# User supplies a price that is within the acceptable range of years but is not the same number.
	# The price will be divisable by 25 with a R of 0. price will alwasy be given first
	# Expectation: autofill will appropreatly fill in all keys and values
	def test_autofill_with_atv_24(self):
		user_list = ["2000","2014", "polaris", "sportsman", "400", "no"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
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
		user_list = ["400","2014", "polaris", "sportsman", "500", "no"]
		autofilled_dict = mod.autofill_vehicle(user_list, the_data)
		self.assertEqual("2014", 		autofilled_dict["year"])
		self.assertEqual("polaris", 	autofilled_dict["brand"])
		self.assertEqual("sportsman",	autofilled_dict["model"])
		self.assertEqual("400", 		autofilled_dict["cc_rating"])
		self.assertEqual("no", 			autofilled_dict["awd"])
		self.assertEqual("500", 		autofilled_dict["price"])
		self.assertEqual(6, 			len(autofilled_dict)) # Assure that the dict only has the 6 keys checked above	
		
		
# most_likely will take any number that appears in the users input to determin what that number represents and then
# return the appropriate responce if possible, otherwise will return "cannot_interpret"
class Most_likely(unittest.TestCase):
	
#################################################################################################
							## TESTS THAT FOCUS ON PRICES THAT ARE WITHIN A VALID YEAR RANGE ##
#################################################################################################
	
	# User list will contain an appropreate year, common cc_rating, common price value for brand and model
	# Expected, when most_likly() is given the year value, will return "year", when given the cc value, will return
	# 	"cc_rating", and when the price value is give, will return "price"
	def est_most_likely_1(self): 
		user_list = ["1998", "polaris", "sportsman", "400", "yes", "1800"]
		a_dict = {}
		
		the_dict = {"item" : "1998", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("year", string)
		
		the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)
		
		the_dict = {"item" : "1800", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)		
		
	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate year for brand and model. However, the year and price will NOT be the same number
	# The year if divided by 25 will not have a reminder of 0 but price will.
	# Expected, when most_likly() is given the year value, will return "year", when given the cc value, will return
	# 	"cc_rating", and when the price value is give, will return "price"
	def est_most_likely_2(self):
		user_list = ["1998", "polaris", "sportsman", "400", "yes", "2000"]
		a_dict = {}
		
		the_dict = {"item" : "1998", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("year", string)
		
		the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)
		
		the_dict = {"item" : "2000", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)	

	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate year for brand and model. However, the year and price WILL be the same number
	# and both will be divisable by 25 with a remainder of 0
	# Expected, when most_likly() is given the year value, will return "year", when given the price, will return
	# 	"price", and when the cc_value value is gave, will return "cc_rating"
	def est_most_likely_3(self):
		user_list = ["2000", "polaris", "sportsman", "400", "yes", "2000"]
		a_dict = {}
		
		# Give most_likely an empty dict for a_dict, this should return "year" when two values are present in user_list
		# that are appropreate for  "year" and "price". price IS divisable by 25 with a remainder of 0 and the year IS
		# the same vlaue
		the_dict = {"item" : "2000", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("year", string)
		
		# Assuming the user_list above, a_dict has already been populate with a "year" key and now most_likely is called
		# again with the year value. 
		# Expectation: most_liekly will return "price"
		a_dict = {"year" : "2000"}
		the_dict = {"item" : "2000", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)
		
		
	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate year for brand and model. However, the year and price WILL be the same number
	# and both will NOT be divisable by 25 with a remainder of 0
	# Expected, when most_likly() is given the year value, will return "year", when given the price, will return
	# 	"price", and when the cc_value value is gave, will return "cc_rating"
	def est_most_likely_4(self):
		user_list = ["1999", "polaris", "sportsman", "400", "yes", "1999"]
		a_dict = {}
		
		# Give most_likely an empty dict for a_dict, this should return "year" when two values are present in user_list
		# that are appropreate for  "year" and "price". price IS divisable by 25 with a remainder of 0 and the year IS
		# the same vlaue
		the_dict = {"item" : "1999", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("year", string)
		
		# Assuming the user_list above, a_dict has already been populate with a "year" key and now most_likely is called
		# again with the year value. 
		# Expectation: most_liekly will return "price"
		a_dict = {"year" : "2000"}
		the_dict = {"item" : "1999", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)	
	
	
		the_dict = {"item" : "400", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)
	
	
	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate year for brand and model. However, the year and price WILL NOT be the same number
	# and both will NOT be divisable by 25 with a remainder of 0
	# Expected, when most_likly() is given the year value, will return "cannot_interpret", when given the price, will return
	# 	"cannot_interpret", and when the cc_value value is gave, will return "cc_rating"
	def est_most_likely_5(self):
		user_list = ["1997", "polaris", "sportsman", "400", "yes", "1998"]
		
		a_dict = {}
		the_dict = {"item" : "1997", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cannot_interpret", string)
		
		a_dict = {}
		the_dict = {"item" : "1998", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cannot_interpret", string)
		
		a_dict = {}
		the_dict = {"item" : "400", "users_list" : user_list, "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)

##################################################################################################
								## TESTS THAT FOCUS ON PRICES THAT ARE WITHIN A VALID CC RANGE ##
##################################################################################################
		
	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate cc_rating for brand and model. However, the year and cc_rating will NOT be the same 
	# number
	# Expected, when most_likly() is given the year value, will return "year", when given the price, will return
	# 	"price", and when the cc_value value is gave, will return "cc_rating"
	def est_most_likely_6(self):
		user_list = ["1998", "polaris", "sportsman", "400", "yes", "450"]
		a_dict = {}
		
		the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)		

		the_dict = {"item" : "450", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)	
	
	# User list will contain an appropreate year, common cc_rating, and a price value that falls within the range 
	# for an appropriate cc_rating for brand and model. However, the year and cc_rating WILL be the same 
	# number
	# Expected, when most_likly() is given the year value, will return "year", when given the price, will return
	# 	"price", and when the cc_value value is gave, will return "cc_rating"
	def est_most_likely_7(self):
		user_list = ["1998", "polaris", "sportsman", "400", "yes", "400"]
		a_dict = {}
		
		the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("cc_rating", string)
		
		a_dict = {"cc_rating" : "400"}
		the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		string  = mod.most_likely(the_dict, the_data)
		self.assertEqual("price", string)
	
	#def test_most_likely_8(self):
		#user_list = ["2007", "encore", "xtreme", "52", "500"]
		#a_dict = {}
		
		#the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		#string  = mod.most_likely(the_dict, the_data)
		#self.assertEqual("cc_rating", string)
		
		#a_dict = {"cc_rating" : "400"}
		#the_dict = {"item" : "400", "users_list" : user_list,  "a_dict" : a_dict}
		#string  = mod.most_likely(the_dict, the_data)
		#self.assertEqual("price", string)
	
	
	
	
	
	
	
	
	
	
	

if __name__ == '__main__':
    unittest.main()
