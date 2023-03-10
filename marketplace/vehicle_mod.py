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
def confirm_vehicle(vehicle):
	
	if vehicle.get_awd() == "yes": is_awd = " with 4X4 "
	else: is_awd 	= " without 4X4 "
	
	message = (  " " 			+ vehicle.get_year() 
						+ " " 			+ vehicle.get_brand().title() 
						+ " " 			+ vehicle.get_model().title() 
						+ " " 			+ vehicle.get_cc_rating() 
						+ "CC" 		+ is_awd 
						+ "for $" 	+ vehicle.get_price())
	return message

# TESTED - Given the needed paramiters, creates and returns an vehicle object
def make_vehicle(year, brand, model, cc_rating, awd, price, classification = "All Terain Vehicle"):
									
	new_vehicle = Atv( year = year.replace(" ", "").lower(), 
										brand = brand.strip().lower(), 
										model = model.strip().lower(), 
										cc_rating = cc_rating.replace(" ", "").lower(),
										awd = awd.replace(" ", "").lower(), 
										price = price.replace(" ", "").lower(),
										classification = classification)
	return new_vehicle
	
	
	
	
	
	
	
	
