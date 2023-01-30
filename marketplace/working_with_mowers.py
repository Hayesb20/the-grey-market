# Brian Hayes
# 04 Jan 2023

# This module should contain all functions that will ask the use for input
# See working_with_atv_modules for functions that only use known
# parameters

from mower_class 			import Mower
from handeling_strings 	import parse
from auto_fill_mod 			import autofill_atv


def build_mower():
	string = input(" Sounds good, tell me about this mower "
				+ "\n I need to know the brand, Hp, deck size, "
				+ "\n what kind of mower it is (pushmower, zero turn etc)"
				+ "\n and I need to know how much it is of course\n")
				
	my_list = parse(string)
	
	#Takes a list and returns a dictionary
	a_dict = wwam.autofill_atv(	my_list, 
											database = known_brands_and_models,
											models_and_their_cc = models_and_their_cc)


def work_with_mowers(): # This is basically the main function
	
		j = 0
		
		while j < 1:
			
			#Asks the user for the needed information to make a new mower
			new_mower = build_mower()
			j = j + 1
