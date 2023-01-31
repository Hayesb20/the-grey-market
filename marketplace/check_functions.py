#Brian Hayes
# 16 Nov 2022

affirmative_words 	= ["y", "yes", "yea", "yeah", "mhm", "of course", "yes please", "ye",
										"same"]
									
words_of_denial 		= ["no", "n", "nope", "nay", "not", "ni", "np", "nothing", "nothin",
										"different one", "diff", "another", "stop", "nvm", "done", "nop",
										"close", "im done", "i'm done", "close app"]

search_words 			= ["look up", "search", "find"]
								
# atv_words 				= ["atv", "quad", "quads", "wheelers", "four wheelers", "atvs", "ats"]

#mower_word 			= ["mower", "mow"]

show_words				= ["show database", "show", "see", "see database", "see data", "show data"]


# TESTED - Takes a string and a dictionary and returns True or False depending on if the string appears as a key in the dict
def check_brand(brand, a_dict):
	for thing in a_dict:
		if brand == thing.get_brand():
			return True
	return False

# TESTED - Update to take a database to check for the brand&model
def check_model(model, a_dict):
	for thing in a_dict:
		if model == thing.get_model():
			return True
	return False

# TESTED - Takes a string and returns another string based uplon what the given string is
def check_answer(answer):
	if 	answer.lower() 	in affirmative_words: 				return "yes"
	elif 	answer.lower() 	in words_of_denial: 					return "no"
	elif  answer.lower()		in search_words:							return "search"
#	elif 	answer.lower()		in atv_words:								return "atv_word"
#	elif 	answer.lower()		in mower_word:							return "mower_word"
	elif 	answer.lower() 	in show_words:							return "show_database"
	elif  answer.lower()		== "vehicles":								return "vehicle_word"
	elif  answer.lower()		== "open log":								return "open_log"
	elif 	answer.lower()		== "backup":								return "backup"
	elif 	answer.lower()		== "load backup":						return "load_backup"
	elif  answer.lower()		== "add filter":								return "add_filter"
	elif  answer.lower()		== "remove filters":					return "remove_filters"
	elif  answer.lower() 	== "price info" :							return "price_info"
	
	else: 																						return "other"
	
# NOT TESTED
def is_in_database(item, database):
	if database:
		for thing in database:
			if thing.get_essence() == item.get_essence(): return True
	else: return False
	
