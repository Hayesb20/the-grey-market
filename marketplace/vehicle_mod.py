#Brian Hayes
# 17 Nov 2022

import check_functions 	as CF
from atv_class 					import Atv
from mower_class				import Mower

#-----------------------------------------------------------------------------------#
# The above print to console... aka they are not testable
# May be a good idea to either refactor them or return 
# them to working_with_atvs.py
#-----------------------------------------------------------------------------------#

# TESTED - Takes an etv abject and returns a formatted message to ask the user if
# everything is correct
def confirm_vehicle(vehicle):

	# Default Values
	year = ""
	band_model = ""
	engine_size = ""
	awd = ""
	price = ""
	engine_brand = "Engine, "
	deck = ""

	# Get the vehicles information
	a_dict = vehicle.get_essence_as_dict()
	
	# Brand, Model, and Price are assumed to always be present
	band_model = " {brand} {model} ".format(**a_dict)
	price =  "for ${price}".format(**a_dict)
	
	# Cycle through all keys to match values if possible
	for key in a_dict:
		# Format awd verbage if possible
		if key == "awd" and a_dict[key] != "unknown":
			if vehicle.get_awd() == "yes": is_awd = "with 4X4 "
			else: is_awd 	= "without 4X4 "
			awd = is_awd
		
		elif key == "engine_brand" 	and a_dict[key] != "unknown": engine_brand 	= a_dict[key].title() + " Engine, "	# Format engine brand verbage if possible
		elif key == "deck_size"			and a_dict[key] != "unknown": deck 					= a_dict[key] + '" deck '					# Format deck verbage if possible
		elif key == "cc_rating" 			and a_dict[key] != "unknown": engine_size		= "with a " + a_dict[key] + "CC "	# Format engine power verbage if possible
		elif key == "hp_rating" 			and a_dict[key] != "unknown": engine_size 	= "with a " + a_dict[key] + "HP "	# Foremat engine power verbage if possible
		elif key == "year" 					and a_dict[key] != "unknown": year 					= a_dict[key]									# Format year verbage if possible
		
	# Special case: No engine info known | Change verbage as needed
	if "cc_rating" not in a_dict and "hp_rating" not in a_dict and "engine_brand" not in a_dict:
		engine_brand = ""		
		deck = "with a " + deck
	
	
	# Return a string made up of each piece of information. Some pieces can be empty strings
	return " " + year + band_model.title() + engine_size + engine_brand + awd + deck + price



# TESTED - Given the needed paramiters, creates and returns an vehicle object
def make_vehicle(**kwargs):
									
	if kwargs["classification"] == "all terain vehicle" or kwargs["classification"] == "four wheeler":	new_vehicle = Atv( **kwargs)
	if (kwargs["classification"] == "mower"
		or kwargs["classification"] == "riding mower"
		or kwargs["classification"] == "zero turn"):	new_vehicle = Mower(**kwargs)
	return new_vehicle
	
	
	
	
	
	
	
	
