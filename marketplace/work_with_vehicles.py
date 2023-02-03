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
	
	try: 		year = a_dict["year"]
	except: 	year = input("\n What is the year of the vehicle? ")
		
	try: 		brand = a_dict["brand"]
	except: 	brand = get_brand(vehicle_database)
		
	try: 		model = a_dict["model"]
	except: 	model = get_model(vehicle_database)

	try: 		awd = a_dict["awd"]
	except: 	awd = input("\n Does it have awd or 4X4 ")
		
	try: 		price = a_dict["price"]	
	except: 	price = input("\n How much is it? ")
	
	for thing in vehicle_database:
		if a_dict["brand"] == thing.get_brand() and a_dict["model"] == thing.get_model():
			try: 		classification = thing.get_classification()
			except:	classification = input("\n What is this thing exactly? a car or a four wheeler maybe? ")
			
	if classification == "All Terain Vehicle" or classification.title() == "Four Wheeler":
		try: 		cc_rating = a_dict["cc_rating"]
		except: 	cc_rating = input("\n Do you know how many CCs? ")
		new_vehicle = VM.make_vehicle(	year 		 = year.strip(), 
																	brand		 = brand.strip().lower(), 
																	model 	 = model.strip().lower(), 
																	cc_rating= cc_rating.strip(), 
																	awd 	     = awd.strip().lower(), 
																	price 		 = price.strip(),
																	classification = classification.lower())
	
	if classification == "Mower" or classification == "Zero Turn" or classification == "Riding Mower" or classification == "Push Mower":
		# need clever stuff to determin if this needs CC rating or a HP rating
		try: 		cc_rating = a_dict["cc_rating"]
		except: 	cc_rating = input("\n Do you know how many CCs? ")
		# What if the user replies "no"?
		try: 		engine_brand = a_dict["engine_brand"]
		except: 	engine_brand = input("\n Do you know what brand the engine is? ")
		new_vehicle = Mower(**a_dict)
	
	
	
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
				print ("No database to show")
			except: print (" Okay, there it is")
	
		elif CF.check_answer(answer) == "load_backup":
			# Add some sort of warning message about potential data loss and add an option to cancel
			while vehicle_database != []: vehicle_database.pop()
			try: 
				load_file(	database = vehicle_database, filename = dict_of_filepaths["filepath_to_vehicle_database_backup.txt"])
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
						new_vehicle	= build_vehicle(database = vehicle_database)
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














