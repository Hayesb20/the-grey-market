# Brian Hayes
#16 Nov 2022

import ast

from atv_class import Atv
from auto_fill_mod import autofill_vehicle
from datetime import datetime

dict_of_filepaths = {
								"filepath_to_vehicle_database.txt" 					: "txt_files/vehicle_database.txt",
								"filepath_to_vehicle_database_backup.txt"	: "txt_files/vehicle_database_backup.txt",
							}

# TESTED - given a file name and a database, will figure out which loading method to call
def load_file(database, filename):				
	
	if filename == dict_of_filepaths["filepath_to_vehicle_database.txt"]:
		database = load_file_helper(database, filename)
		
	elif filename == dict_of_filepaths["filepath_to_vehicle_database_backup.txt"]:
		database = load_file_helper(database, filename)
		
	return database
			
#NOT TESTED - Takes an empty list and filename, will load the list with contence of file (atvs)	
def load_file_helper(database, filename):
	with open(filename, "r") as file_object:
		contence = file_object.read()
		database = []
		a_word = ""
		while contence != "":

			if contence[0] != "\n":
				a_word = a_word + contence[0]
				contence = contence[1:]
				
			elif contence[0] == "\n":
				kwargs = ast.literal_eval(a_word)
				newVehicle = Atv(**kwargs)
				database.append(newVehicle)	
				a_word = ""
				contence = contence[1:]	
	return database
	
	
	
			
# NOT TESTED - Will use a filename to determin which sub function needs to be called		
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
	
# NOT TESTED - Given the atv_database list, returns a string
def convert_objects_in_atv_database_to_a_string(list_of_objects):
	string = ""
	for thing in list_of_objects:
		string = string + str(thing.get_essence_as_dict()) + "\n"
	return string
		
		

# NOT TESTED - Returns a string that contains information about an ATV to be orinted		
#needs to actually return a string to be printed. not print itself
def show_database(database):
	for item in database:
		print(item.get_essence())
			
