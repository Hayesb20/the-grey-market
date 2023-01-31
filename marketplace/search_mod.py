# Brian Hayes
# 23 Jan 2023

from handeling_strings 		import parse
from load_and_save_files import load_file, dict_of_filepaths, show_database
from check_functions 		import check_answer


atv_database = []

def load_files():
	# Look for a txt file at the designated location to use
	try:	load_file(	database = atv_database,
							filename = dict_of_filepaths["filepath_to_atv_database_txt"])
	except: print(" Failed to load 'atv_database.txt'")	
	else: print(" Database loaded successfully")	

def is_valid_thing(a_list, a_word):
	for i in range(len(a_list)):
		if a_word == a_list[i]: return True
	return False

def filter_data(list_of_users_words):
		a = 0
		while a < len(atv_database):
			for i in range(len(list_of_users_words)):
				if is_valid_thing(atv_database[a].get_essence(), list_of_users_words[i]): a = a + 1
				else: del atv_database[a]
	
def show_price_info():
	the_sum = 0
	largest = 0
	smallest = 100000
	for thing in atv_database:
		if int(thing.get_price()) > largest: largest = int(thing.get_price()) 
		if int(thing.get_price()) < smallest: smallest = int(thing.get_price())
		the_sum = the_sum + int(thing.get_price())
			
	print("\n The most expensive item in the list is $", largest)
	print(" The least expensive item in the list is $", smallest)
	print(" And the average price is $", int(the_sum/len(atv_database)))
	
def options():
	options_list = ["\n Done : to stop looking up items",
								" Price Info : I'll show you the highest, average, and lowest price of everything",#NOT DONE
								" Add Filter : we can add another filter and narrow the list down further",
								" Remove Filters : we can remove all filters and start fresh", 
								" Show: You can see a list based on the filters you gave "] 
	for option in options_list: print(option)	
	
	
def search_item ():
	
	load_files()

	i = 0
	while i <= 1:
		options()
		answer = input ( " Okay lets start. Where should we start? \n ")	
		
		word = check_answer(answer)
		match word:
			case "no" 							: return
			case "add_filter" 				: filter_data(parse(input(" what would you like to filter by? \n ")))
			case "show_database" 	: show_database(atv_database)
			case "remove_filters" 		: load_files()
			case "price_info"				: show_price_info()

			
			
		
		
		
		
		
		 
	
