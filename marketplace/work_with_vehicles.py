# Brian Hayes
# 17 Nov 2022

import check_functions 		as CF
import vehicle_mod				as VM

from vehicle_statistic_mod 	import get_statistical_data
from handeling_strings 			import parse
from auto_fill_mod 				import autofill_vehicle
from load_and_save_files 	import load_file, save_file, dict_of_filepaths, show_database

from mower_class import Mower


def get_brand(vehicle_database):
	brand = input("\n What is the brand? ")
	brand = brand.strip().lower()
	
	while not CF.check_brand(brand, vehicle_database):
		answer = input("\n I do not recognize that brand. Are you sure its correct? ")
		if CF.check_answer(answer) == "yes":
			print ("\n Okay, just wanted to make sure ")
			return brand
			
		elif CF.check_answer(answer) == "no": 
			brand = input("\n Okay, no problem, just tell me the brand again ")
			
	return brand

def get_model(vehicle_database):	
	model = input ("\n What is the model? ")
	model = model.strip().lower()

	while not CF.check_model(model = model, a_dict = vehicle_database):
		answer = input ("\n I do not recognize this model? Are you sure its correct? ")
		if CF.check_answer(answer) == "yes"	: 
			print ("\n Okay, just wanted to make sure ")	
			return model
		elif CF.check_answer(answer) == "no"	: model = input("\n Okay, no problem, just tell me the model again ")	
	return model
	
def is_same_thing(item):
	print ("\n Ah yes! I remember that one!")
	answer = input("\n Are they different? ")
	answer = CF.check_answer(answer)
	
	if answer == "no": print ("\n Same one? Okay, I won't remember it then ")
	elif answer == "yes" :
		print("\n Okay!, i'll record this one too")
		vehicle_database.append(item)
	elif answer == "other": is_same_thing()

def should_I_remember(answer, item, vehicle_database):
	answer = CF.check_answer(answer)
	if answer == "yes":
		print("\n Okay")
		vehicle_database.append(item)
							
	elif answer == "no": print("\n Consider it forgotten. ")
		
	elif answer == "other":
		answer = input("\n I'm afraid I didn't understand. Do you want me to record it? ")
		should_I_remember(answer, item, vehicle_database)
	
def build_vehicle(vehicle_database):
	string = input("\n Cool, tell me about this vehicle "
								+ "\n I need the Brand, Price, Year, and Model of your vehicle"
								+ "\n and any other information you have about it. If there"
								+ "\n is anything else I need i'll ask!"
								+ "\n Please be sure to use spaces between words\n ")

	if CF.check_answer(string) == "no": return "no object made"
	my_list = parse(string)
	
	#Takes a list and returns a dictionary
	a_dict = autofill_vehicle(my_list, database = vehicle_database)
	print(a_dict)
	
	if "year" not in a_dict:
		if(CF.check_answer(input(" Do you know the year of your vehicles?\n ")) == "no"):
			pass
		else: a_dict["year"] = input("\n What is the year of the vehicle? ")
		
	if "brand" not in a_dict:
		a_dict["brand"] = get_brand(vehicle_database)
		
	if "model" not in a_dict:	
	 	a_dict["model"] = get_model(vehicle_database)
		
	if "price" not in a_dict:
		a_dict["price"] = input("\n How much is it? ")
	
	# Try to automatically fill in the classification variable without asking the user
	for thing in vehicle_database:
		if a_dict["brand"] == thing.get_brand() and a_dict["model"] == thing.get_model():
			a_dict["classification"] = thing.get_classification()
	
	if "classification" not in a_dict:
		a_dict["classification"] = input("\n What is this thing exactly? a car or a four wheeler maybe? ")


	# Decision tree - should probably be its own function
	if a_dict["classification"] == "all terain vehicle" or a_dict["classification"].title() == "four wheeler":
		if "cc_rating" not in a_dict:
		 	a_dict["cc_rating"] = input("\n Do you know how many CCs? ")
		if "awd" not in a_dict:	
			a_dict["awd"] = input("\n Does it have awd or 4X4 ") # Should add protection against inappropreate values
		
		new_vehicle = VM.make_vehicle(** a_dict)
	
	if a_dict["classification"] == "mower" or a_dict["classification"] == "zero turn" or a_dict["classification"] == "riding mower" or a_dict["classification"] == "push mower":
		# Need clever stuff to determin if this needs CC rating or a HP rating
		if "cc_rating" not in a_dict:
			answer = input("\n Do you know how many CCs? ")
			if CF.check_answer(answer) != "no":
				temp_answer = input("is this cc or hp? ")
				if temp_answer == "cc":
					a_dict["cc_rating"] = str(answer)
				else: 	a_dict["hp_rating"] = str(answer)
		# What if the user replies "no"?
		if "engine_brand" not in a_dict:
			answer = input("\n Do you know what brand the engine is? ")
			if CF.check_answer(answer) != "no":
				a_dict["engine_brand"] = str(answer)
		 			
		if "deck_size" not in a_dict:
			answer = input("\n Do you know what size the deck is? ")
			if CF.check_answer(answer) != "no":
				a_dict["deck_size"] = str(answer)
		
		print(a_dict)
		new_vehicle = Mower(**a_dict) # should be something like VM.makevehicles
	
	
	
	VM.confirm_vehicle(new_vehicle)
	return new_vehicle

def load_files():
	# Look for a txt file at the designated location to use
	try: 
		database = load_file(filename = dict_of_filepaths["filepath_to_vehicle_database.txt"])
		print(" Database loaded successfully")	
		return database
	except: print(" Failed to load 'vehicle_database.txt'")	
	

def save_files(vehicle_database):
	try : 
		save_file(	database = vehicle_database, 
						filename =  dict_of_filepaths["filepath_to_vehicle_database.txt"])
		print(" Database saved successfully")	
	except: print(" Failed to save 'vehicle_database.txt'")
	

def options():
	options_list = ["\n Show database : I will show you all the vehicles I know of",
							" Load Backup : I will load my most recent backup",
							" Backup : I will update by backup files",
							" Stop : We will return to the privious page",
							" Open Log : We can add new vehicles to our record" ]

	for option in options_list: print(option)

def work_with_vehicles():
	
	vehicle_database = load_files()	
	print("1")
	z = 0
	while z < 1:
		options()
		answer = input(" What do you need?\n ")
		if CF.check_answer(answer) == "no": 
			save_files(vehicle_database)
			z = 1
		
		elif CF.check_answer(answer) == "other": 
			options()
			answer = input ("\n Sorry, what did you want to do? \n  ")
	
		elif CF.check_answer(answer) == "show_database":
			try: 
				show_database(vehicle_database)
				print (" Okay, there it is")
			except: print ("No database to show")
	
		elif CF.check_answer(answer) == "load_backup":
			# Add some sort of warning message about potential data loss and add an option to cancel
			while vehicle_database != []: vehicle_database.pop()
			try: 
				load_file(filename = dict_of_filepaths["filepath_to_vehicle_database_backup.txt"])
				save_files(vehicle_database)
			except: 	print("Failed to load 'atv_database_backup.txt'")				
			else: 		print(" Databased loaded successfully")
		
			options()
			answer = input ("\n Okay then, is there something else you want to look at? ")
	
		elif CF.check_answer(answer) == "backup":
			try:
				save_file(	database = vehicle_database, 
									filename = dict_of_filepaths["filepath_to_vehicle_database_backup.txt"])
				print("Backup Successful")
			except: print("Backup Failed")
	
		elif CF.check_answer(answer) == "open_log":
		
			j = 0
			print("\n Okay, let's go check out this vehicle of yours")
			while j < 1:
						
				#Asks the user for the needed information to make a new vehicle
				new_vehicle = build_vehicle(vehicle_database = vehicle_database) 
				
				if new_vehicle == "no object made": 
					print(" Okay no problem \n Is there something else we can do here? \n")
					break
									
				# Ask the user to assure the input
				print ("\n Okay great!, let's make sure I got that right, you have a")
				print(VM.confirm_vehicle(new_vehicle))
				answer = input(" Is this correct? (Yes/No) ")
				answer = CF.check_answer(answer)
			
				while answer != "yes":
					if answer == "no":
						new_vehicle	= build_vehicle(vehicle_database)
						print (VM.confirm_vehicle(new_vehicle))
						answer	= input(" Is this correct? (Yes/No) ")
						answer	= CF.check_answer(answer)
				
					else: answer = input(" I'm afraid i didn't understand." + 
								" Is this summary correct? (Yes/No) ")
						
				# Return to the user information about the atv they have if possible. 
				# Information to be returned: What is its price relative to other ATVs of the 
				# same year, brand and model. Also show how it compares to ATVs of the 
				# same brand and model only.
				answer = input("\n Would you like to see how the atv you just told me \n"
										+ " about compares to what I can find out? ")
				if CF.check_answer(answer) == "yes": print("\n" + get_statistical_data(new_vehicle, vehicle_database))
				
				#Look up and see if the atv already exists in the database and then checks
				# to see what the user wants to do with the atv they created
				answer = CF.is_in_database(new_vehicle, vehicle_database)
				if answer == True: is_same_thing(new_vehicle)
				
				else:
					answer = input("\n It seems this a new one, should I remember it? ")
					should_I_remember(answer, new_vehicle, vehicle_database)
					save_files(vehicle_database)
						
				# Checks to see if the user would like to enter in another ATV
				answer = input("\n Do you have another in mind? ")
				if CF.check_answer(answer) == "yes": print("\n great!")
				elif CF.check_answer(answer) == "no": break
				else : j = j+1
	
	return 














