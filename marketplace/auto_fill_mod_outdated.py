#Brian Hayes
#16 Nov 2022

from datetime import date
import math


def most_likely(the_dict, database):
	
	if int(the_dict["item"]) > int(date.today().year): return "price"
	elif int(the_dict["item"]) > 1000 and int(the_dict["item"]) < 1950: return "price" # 1000 cc_rating cannot be autocorrected for. Will not track anything older than 1950AD
####################################################################
                   ## Code that deals with prices being in the range of years ##
####################################################################	
	list_of_possible_years = []
	for string in the_dict["users_list"]:
		try: 
			if int(string) >= 1950 and int(string) <= date.today().year: list_of_possible_years.append(int(string))
		except: i = 1
		
	# If there is only 1 number in the appropreate year range, return year 
	# If user does not give a year, then price will be used if it meets the requirements	
	if (len(list_of_possible_years) == 1 
		and int(list_of_possible_years[0]) == int(the_dict["item"])): 
			return "year"
	
	# If the user gives values for both year and price but both values fall within the range of appropreate years
	# the two values ARE NOT == to one another but one value IS divisabe by 25 with a remainder of 0

	if (len(list_of_possible_years) == 2 
		and int(list_of_possible_years[0]) != int(list_of_possible_years[1])  # Affirm the two values aree not ==
		and int(the_dict["item"]) > 1000 ): 															# Affirm that "item" is not a cc_rating !!NOTE!! the 1000 should be dynamic andscale depending on what we are working with
			# If neither number
			if (math.remainder(int(list_of_possible_years[0]), 25 )!= 0				# Affirm that the first possibility will not have a remainder of 0 if divided by 25
				and math.remainder(int(list_of_possible_years[1]), 25) != 0):		# Affirm that the second possibility will not have a remainder of 0 if divided by 25
					return "cannot_interpret"																	# If neither possibility would have a reminder of 0 then an educated guess cannot be made
			# If the first number
			elif (math.remainder(int(list_of_possible_years[0]), 25 ) == 0			# Affirm that the first possibility will  have a remainder of 0 if divided by 25
				and math.remainder(int(list_of_possible_years[1]), 25) != 0):		# Affirm that the second possibility will not have a remainder of 0 if divided by 25
					if int(the_dict["item"]) == int(list_of_possible_years[0]):			# Is "item" the first number
						return "price"																					# If it is then logically it is probably the "price"
					elif int(the_dict["item"]) == int(list_of_possible_years[1]):		# Is "item" the second number
						return "year"																					# If it is then logically it is probably the "year"
			# If the second number
			elif (math.remainder(int(list_of_possible_years[0]), 25 )!= 0			# Affirm that the first possibility will not have a remainder of 0 if divided by 25
				and math.remainder(int(list_of_possible_years[1]), 25) == 0):		# Affirm that the second possibility will  have a remainder of 0 if divided by 25
					if int(the_dict["item"]) == int(list_of_possible_years[0]):			# Is "item" the first number
						return "year"																					# If it is then logically it is probably the "year"
					elif int(the_dict["item"]) == int(list_of_possible_years[1]):		# Is "item" the second number
						return "price"																					# If it is then logically it is probably the "price"
	
			
	# If the user gives values for both year and price but both values fall within the range of appropreate years
	# and the two values ARE  == to one another
	if (len(list_of_possible_years) == 2 
		and int(list_of_possible_years[0]) == int(list_of_possible_years[1])	# Affirm that the two values are == to one another
		and int(the_dict["item"]) > 1000):																# Afform that "item" is not a cc_rating
		try:
			temp_dict = the_dict["a_dict"]																	# Check to see if the_dict already has a "year" key	
			if temp_dict["year"] : return "price"														# If it does then "item" must be the "price"
		except: return "year"																						# Otherwise "item" must be the "year"
	

		
#########################################################
	## Code that deals with prices being within the range of cc_ratings
#########################################################
	list_of_possible_CCs = []
	for string in the_dict["users_list"]:
		try:
			if int(string) <= 1000: list_of_possible_CCs.append(int(string))
		except: i = 1		
		
	if (len(list_of_possible_CCs) == 1 
		and int(list_of_possible_CCs[0]) == int(the_dict["item"])): 
			return "cc_rating"	
	
	# The two numbers are NOT the same
	if (len(list_of_possible_CCs) == 2 
		and int(list_of_possible_CCs[0]) != int(list_of_possible_CCs[1])):			
		cc_occurence_counter = 0
		price_occurence_counter = 0
		for thing in database:
			
			if (int(list_of_possible_CCs[0]) == int(thing.get_cc_rating())
				and int(list_of_possible_CCs[0] == int(the_dict["item"]))):
					cc_occurence_counter = cc_occurence_counter + 1
				
			elif (int(list_of_possible_CCs[0]) == int(thing.get_cc_rating())
				and int(list_of_possible_CCs[0] == int(the_dict["item"]))):
					cc_occurence_counter = cc_occurence_counter + 1
				
			elif (int(list_of_possible_CCs[1]) == int(thing.get_price())
				and int(list_of_possible_CCs[1] == int(the_dict["item"]))):
					price_occurence_counter = price_occurence_counter + 1
				
			elif (int(list_of_possible_CCs[1]) == int(thing.get_price())
					and int(list_of_possible_CCs[1] == int(the_dict["item"]))):
					price_occurence_counter = price_occurence_counter + 1

		if int(the_dict["item"]) == int(list_of_possible_CCs[0]) 	and cc_occurence_counter > price_occurence_counter: 	return "cc_rating"
		elif int(the_dict["item"]) == int(list_of_possible_CCs[0]) and cc_occurence_counter < price_occurence_counter: 	return "price"
		elif int(the_dict["item"]) == int(list_of_possible_CCs[1]) and cc_occurence_counter > price_occurence_counter: 	return "cc_rating"
		elif int(the_dict["item"]) == int(list_of_possible_CCs[1]) and cc_occurence_counter < price_occurence_counter: 	return "price"		
		elif int(the_dict["item"]) == int(list_of_possible_CCs[1]) and cc_occurence_counter == price_occurence_counter: 	return "cannot_interpret"	
		else: return "cannot_interpret"

	# The two numbers ARE the same
	if	(len(list_of_possible_CCs) == 2
		and int(list_of_possible_CCs[0]) == int(list_of_possible_CCs[1])):
			try:
				temp_dict = the_dict["a_dict"]
				if temp_dict["cc_rating"] : return "price"
			except: return "cc_rating"

def is_complete(users_list, a_dict):
	counter = 0
	my_list = [*set(users_list)]
	for item in my_list:
		for key in a_dict:
			if a_dict[key] == item: counter = counter + 1
	if counter == len(users_list): return True
	else: return False
	
# a_list is a list with strings that represent information about the object the user wants to create			
# database will be a list of known objects 
def autofill_vehicle(users_list, database):
	
	a_dict = {}
	for thing in database:
		temp_dict =  thing.get_essence_as_dict()
		for item in users_list:
			for key in temp_dict:
				if item.isnumeric():
					most_likelys_dict = {"item" : item, "users_list" : users_list, "a_dict" : a_dict}
					a_dict[most_likely(most_likelys_dict, database)] = item
												
				elif item == temp_dict[key]:
					a_dict[key] = item	

		if is_complete(users_list, a_dict): return a_dict
		
	
				
	return a_dict
