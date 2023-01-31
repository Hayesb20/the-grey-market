# This file should contain only those functions that will be used
# by more than 1 file that are pertaining to unrelated sections of
# the program



def parse(string):
	len_of_string = len(string)
	counter = 0
	unknown_word = ""
	a_list = []
	
	while string != "":	
		counter = counter + 1
		if string[0] == " " or counter == len_of_string:
			if counter == len_of_string: unknown_word = unknown_word + string[0]	
			a_list.append( unknown_word.lower())
			unknown_word = ""
		else: unknown_word = unknown_word + string[0]
		string = string[1:]
						
	return a_list
