# Brian Hayes
# 31-Oct-2022


# TO-DO 
# This file doe not need to open and save files. Each moduel that works with a group of functions
# like working_with_atvs should open and save the files that it needs

import main_modules as mod


from check_functions 			import check_answer
from load_and_save_files 	import load_file
from load_and_save_files 	import save_file
from load_and_save_files 	import dict_of_filepaths
from working_with_atvs		import work_with_atvs
from working_with_mowers import work_with_mowers
from search_mod					import search_item


# For better or worse, these global variabls are being updated through various
# functions. I may want to consier revamping the functions to take these as
# local variables and paramiters. this might allow for easier creation and usage
# of multiple classes in addition to the ATV class. 


def options():
	options_list = ["\n Search : Tell me about an item and I will tell you everything I know about it", # User can ask about an item # NOT CODED
							" Atv : will allow you to price check, or add a new atv", 
							" Mower : will allow you to price check, or add a new mower",
							" No : to close the app"]
	for option in options_list: print(option)


def main():
		
	i = 0
	while i < 1:
		options()
		answer = input ("\n What would you like to do ? ")
		word = check_answer(answer)
		
		match word:
			case "search" : search_item()
			case "atv_word": work_with_atvs()
			case "mower_word": work_with_mowers()
			case "no": i = i+1
			case "other": print ("\n I'm sorry, I don't seem to know what that is")

						

if __name__ == '__main__': main()
	
