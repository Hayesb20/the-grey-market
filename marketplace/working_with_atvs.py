# Brian Hayes
# 17 Nov 2022

import main_modules
import check_functions 						as CF
import working_with_atvs_modules 	as wwam

from atv_statistic_modules 	import get_statistical_data
from handeling_strings 			import parse
from auto_fill_mod 				import autofill_atv

from load_and_save_files 	import load_file, save_file, dict_of_filepaths, show_database


atv_database = []


def get_brand():
	brand = input("\n What is the brand? ")
	brand = brand.strip().lower()
	
	while not CF.check_brand(brand, atv_database):
		answer = input("\n I do not recognize that brand. Are you sure its correct? ")
		if CF.check_answer(answer) == "yes":
			print ("\n Okay, just wanted to make sure ")
			return brand
			
		elif CF.check_answer(answer) == "no": 
			brand = input("\n Okay, no problem, just tell me the brand again ")
			
	return brand

def get_model():	
	model = input ("\n What is the model? ")
	model = model.strip().lower()

	while not CF.check_model(model = model, a_dict = atv_database):
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
		atv_database.append(item)
	elif answer == "other": is_same_thing()

def should_I_remember(answer, item, atv_database):
	answer = CF.check_answer(answer)
	if answer == "yes":
		print("\n Okay")
		atv_database.append(item)
							
	elif answer == "no": print("\n Consider it forgotten. ")
		
	elif answer == "other":
		answer = input("\n I'm afraid I didn't understand. Do you want me to record it? ")
		should_I_remember(answer, item, atv_database)
	
def build_atv(database):
	string = input("\n Cool, tell me about this ATV "
								+ "\n I need to know the ATVs year, model, "
								+ "\n brand, engine size, price and whether or not "
								+ "\n it has 4X4 capabilities\n"
								+ "\n Please be sure to use spaces between words\n ")

	if CF.check_answer(string) == "no": return "no object made"
	my_list = parse(string)
	
	#Takes a list and returns a dictionary
	a_dict = autofill_atv(	my_list, database = database)
	
	try: 		year = a_dict["year"]
	except: 	year = input("\n What is the year of the ATV? ")
		
	try: 		brand = a_dict["brand"]
	except: 	brand = get_brand()
		
	try: 		model = a_dict["model"]
	except: 	model = get_model()
		
	try: 		cc_rating = a_dict["cc_rating"]
	except: 	cc_rating = input("\n Do you know how many CCs? ")

	try: 		awd = a_dict["awd"]
	except: 	awd = input("\n Does it have awd or 4X4 ")
		
	try: 		price = a_dict["price"]	
	except: 	price = input("\n How much is it? ")
		

	new_atv = wwam.make_atv(	year 		 = year.strip(), 
														brand		 = brand.strip().lower(), 
														model 	 = model.strip().lower(), 
														cc_rating= cc_rating.strip(), 
														awd 	     = awd.strip().lower(), 
														price 		 = price.strip())
	wwam.confirm_atv(new_atv)
	return new_atv

def load_files():
	# Look for a txt file at the designated location to use
	try:	load_file(	database = atv_database,
							filename = dict_of_filepaths["filepath_to_atv_database_txt"])
	except: print(" Failed to load 'atv_database.txt'")	
	else: print(" Database loaded successfully")	

def save_files():
	try: save_file(	database = atv_database, 
						filename =  dict_of_filepaths["filepath_to_atv_database_txt"])
	except: print(" Failed to save 'atv_database.txt'")
	else: print(" Database saved successfully")	

def options():
	options_list = ["\n Show database : I will show you all the ATVs I know of",
							" Load Backup : I will load my most recent backup",
							" Backup : I will update by backup files",
							" Stop : We will return to the privious page",
							" Open Log : We can talk about some ATVs you want me to remember" ]

	for option in options_list: print(option)

def work_with_atvs():
	
	load_files()
	
	z = 0
	while z < 1:
		options()
		answer = input(" What do you need?\n ")
		if CF.check_answer(answer) == "no": z = 1
		
		elif CF.check_answer(answer) == "other": 
			options()
			answer = input ("\n Sorry, what did you want to do? \n  ")
	
		elif CF.check_answer(answer) == "show_database":
			try:		 	show_database(atv_database)
			except: 	print ("No database to show")
			else: 	 	print (" Okay, there it is")
			options()
			answer = input ("\n What next? ")
	
		elif CF.check_answer(answer) == "load_backup":
			# Add some sort of warning message about potential data loss and add an option to cancel
			while atv_database != []: atv_database.pop()
			try: 
				load_file(	database = atv_database, filename = dict_of_filepaths["filepath_to_atv_database_backup_txt"])
				save_files()
			except: 	print("Failed to load 'atv_database_backup.txt'")				
			else: 		print(" Databased loaded successfully")
		
			options()
			answer = input ("\n Okay then, is there something else you want to look at? ")
	
		elif CF.check_answer(answer) == "backup":
			try:
				save_file(	database = atv_database, 
									filename = dict_of_filepaths["filepath_to_atv_database_backup_txt"])
				print("Backup Successful")
			except: print("Backup Failed")
	
			options()
			answer = input ("\n Okay then, is there something else you want to look at? ")
	
		elif CF.check_answer(answer) == "open_log":
		
			j = 0
			print("\n Okay, let's go check out this ATV of yours")
			while j < 1:
						
				#Asks the user for the needed information to make a new ATV
				new_atv = build_atv(database = atv_database) 
				
				if new_atv == "no object made": 
					print(" Okay no problem \n Is there something else we can do here? \n")
					break
									
				# Ask the user to assure the input
				print ("\n Okay great!, let's make sure I got that right, you have a")
				print(wwam.confirm_atv(new_atv))
				answer = input(" Is this correct? (Yes/No) ")
				answer = CF.check_answer(answer)
			
				while answer != "yes":
					if answer == "no":
						new_atv	= build_atv(database = atv_database)
						print (wwam.confirm_atv(new_atv))
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
				if CF.check_answer(answer) == "yes": print("\n" + get_statistical_data(new_atv, atv_database))
				
				#Look up and see if the atv already exists in the database and then checks
				# to see what the user wants to do with the atv they created
				answer = CF.is_in_database(new_atv, atv_database)
				if answer == True: is_same_thing(new_atv)
				
				else:
					answer = input("\n It seems this a new one, should I remember it? ")
					should_I_remember(answer, new_atv, atv_database)
					save_files()
						
				# Checks to see if the user would like to enter in another ATV
				answer = input("\n Do you have another in mind? ")
				if CF.check_answer(answer) == "yes": print("\n great!")
				elif CF.check_answer(answer) == "no": return
				else : j = j+1
	
	return 














