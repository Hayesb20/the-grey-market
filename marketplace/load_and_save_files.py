# Brian Hayes
#16 Nov 2022

from atv_class import Atv

dict_of_filepaths = {
								"filepath_to_vehicle_database.txt" 					: "txt_files/vehicle_database.txt",
								"filepath_to_vehicle_database_backup.txt"	: "txt_files/vehicle_database_backup.txt",
							}

# TESTED - given a file name and a database, will figure out which loading method to call
def load_file(database, filename):				
	
	if filename == dict_of_filepaths["filepath_to_vehicle_database.txt"]:
		database = load_file(database, filename)
		
	elif filename == dict_of_filepaths["filepath_to_vehicle_database_backup.txt"]:
		database = load_file(database, filename)
		
	return database
			
#NOT TESTED - Takes an empty list and filename, will load the list with contence of file (atvs)	
def load_file(database, filename):
	with open(filename, "r") as file_object:
		contence = file_object.read()
		myList = []
		year = ""
		while contence != "":
			
			if  contence[0] == "\n":
				contence = contence[1:]
			elif contence[0] != ",":
				year = year + contence[0]
				contence = contence[1:]
				
			elif contence[0] == ",":
				if len(myList)<=5: #This is a problem. when a new attribute is added to an atv, this screws up the loading of the file
					myList.append(year)
				else:
					myList.append(year)
					load_atv = Atv(year = myList[0], brand = myList[1], model = myList[2], cc_rating = myList[3], awd = myList[4], price = myList[5], classification = myList[6])
					database.append(load_atv)
					myList = []
				year = ""
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
	
# NOT TESTED - Given the atv_database list, returns a string
def convert_objects_in_atv_database_to_a_string(list_of_objects):
	string = ""
	for thing in list_of_objects:
		string = string + thing.get_year() + ","
		string = string + thing.get_brand() + ","
		string = string + thing.get_model() + ","
		string = string + thing.get_cc_rating() + ","
		string = string + thing.get_awd() + ","
		string = string + thing.get_price() + ","
		string = string + thing.get_classification() + ","
		string = string + thing.get_date_listed() + ","
		string = string + "\n"
	return string
		
		

# NOT TESTED - Returns a string that contains information about an ATV to be orinted		
#needs to actually return a string to be printed. not print itself
def show_database(database):
	for item in database:
		print(item.get_date_listed(), item.get_classification(), item.get_year(), item.get_brand(), item.get_model(), 
							item.get_cc_rating(), item.get_awd(), item.get_price())
			
