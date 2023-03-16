# Brian Hayes
#16 Nov 2022

import ast

from atv_class import Atv

os_string = "C:/Users/hayesb3/Geany 1.38/Program Files/marketplace/the-grey-market/marketplace/"

dict_of_filepaths = {
						"filepath_to_vehicle_database.txt" 			: os_string+"txt_files/vehicle_database.txt",
						"filepath_to_vehicle_database_backup.txt"	: os_string+"txt_files/vehicle_database_backup.txt",
					}

# TESTED - given a file name and a database, will figure out which loading method to call
def load_file(filename):		
	
	if filename == dict_of_filepaths["filepath_to_vehicle_database.txt"]:
		database = load_file_helper(filename)
		
	elif filename == dict_of_filepaths["filepath_to_vehicle_database_backup.txt"]:
		database = load_file_helper(filename)
	return database
			
# TESTED - Takes an empty list and filename, will load the list with contence of file (atvs)	
def load_file_helper(filename):
	try: 
		with open(filename, "r") as file_object:
			contence = file_object.read()
	except: print("invalid filename")
		
	database = []
	a_word = ""
	while contence != "":
		if contence[0] != "\n":
			a_word = a_word + contence[0]
			contence = contence[1:]
	
		elif contence[0] == "\n":	
			try: 
				kwargs = ast.literal_eval(a_word)
				if kwargs["classification"].lower() ==  "all terain vehicle" or kwargs["classification"].lower() == "four wheeler":
					newVehicle = Atv(**kwargs)
					database.append(newVehicle)	
					a_word = ""
					contence = contence[1:]	
				else: contence = contence[1:]	
			except: "Object creation failed"
		else: contence = contence[1:]
	return database
			
# TESTED - Will use a filename to determin which sub function needs to be called		
def save_file(database, filename):
	if filename == dict_of_filepaths["filepath_to_vehicle_database.txt"]:
		with open(filename, "w") as file_object:
			long_string = convert_objects_in_atv_database_to_a_string(database)
			file_object.write(long_string)		
			
	elif filename == dict_of_filepaths["filepath_to_vehicle_database_backup.txt"]:
		with open(filename, "w") as file_object:
			long_string = convert_objects_in_atv_database_to_a_string(database)
			file_object.write(long_string)	

	elif filename == "txt_files/test_txts/test_file_1.txt":
		with open(filename, "w") as file_object:
			long_string = convert_objects_in_atv_database_to_a_string(database)
			file_object.write(long_string)	
	
# TESTED - Given the atv_database list, returns a string
def convert_objects_in_atv_database_to_a_string(list_of_objects):
	string = ""
	for thing in list_of_objects:
		string = string + str(thing.get_essence_as_dict()) + "\n"
	return string
		
		

# NOT TESTED - Returns a string that contains information about an ATV to be orinted		
#needs to actually return a string to be printed. not print itself
def show_database(database):
	for item in database:
		print(item.get_essence_as_dict())
		
			
