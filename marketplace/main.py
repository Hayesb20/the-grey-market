# Brian Hayes
# 31-Oct-2022

from check_functions 			import check_answer
from work_with_vehicles		import work_with_vehicles
from search_mod					import search_item


def options():
	options_list = ["\n Search : Tell me about an item and I will tell you everything I know about it", # User can ask about an item # NOT CODED
							" Vehicles : Will allow you to price check, or add a new vehicle to our records", 
							" No : To close the app"]
	for option in options_list: print(option)


def main():
		
	i = 0
	while i < 1:
		options()
		answer = input ("\n What would you like to do ? ")
		word = check_answer(answer)
		
		match word:
			case "search" : search_item()
			case "vehicle_word": work_with_vehicles()
			case "no": i = i+1
			case "other": print ("\n I'm sorry, I don't seem to know what that is")

						

if __name__ == '__main__': main()
	
