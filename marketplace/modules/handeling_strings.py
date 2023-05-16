

import regex as re



def parse(a_string):

	# Removed any occurances of .0, .00, .000 etc.
	#print(a_string)
	a_string = re.sub(pattern="(?<=[?]*)(?=[0-9]*)[.]0*", repl=" ", string=a_string)
	#print(a_string)
	
	# Removed any occurances when a sentence ends with a . but no space is used before starting
	# the next sentence. E.g. "The dog sat.The sun sat"
	a_string = re.sub(pattern=("(?<=[a-zA-Z0-9])[.](?=[a-zA-Z0-9])"), repl=" ", string=a_string) 


	for char in a_string:
		if (char.isdigit() == False 
      		and char.isalpha() == False 
			and char != " "): 
			a_string = a_string.replace(char, "")
			

	a_list = a_string.lower().split()
	
	return a_list
