#Brian Hayes
# 17 Nov 2022

import check_functions 	as CF
from atv_class 					import Atv

#-----------------------------------------------------------------------------------#
# The above print to console... aka they are not testable
# May be a good idea to either refactor them or return 
# them to working_with_atvs.py
#-----------------------------------------------------------------------------------#

# TESTED - Takes an etv abject and returns a formatted message to ask the user if
# everything is correct
def confirm_atv(atv):
	
	if atv.get_awd() == "yes": is_awd = " with 4X4 "
	else: is_awd 	= " without 4X4 "
	
	message = (  " " 			+ atv.get_year() 
						+ " " 			+ atv.get_brand().title() 
						+ " " 			+ atv.get_model().title() 
						+ " " 			+ atv.get_cc_rating() 
						+ "CC" 		+ is_awd 
						+ "for $" 	+ atv.get_price())
	return message

# TESTED - Given the needed paramiters, creates and returns an atv object
def make_vehicle(year, brand, model, cc_rating, awd, price):
	new_vehicle = Atv(   year.replace(" ", "").lower(), 
								brand.strip().lower(), 
								model.strip().lower(), 
								cc_rating.replace(" ", "").lower(),
								awd.replace(" ", "").lower(), 
								price.replace(" ", "").lower())
	return new_vehicle
	
	
	
	
	
	
	
	
