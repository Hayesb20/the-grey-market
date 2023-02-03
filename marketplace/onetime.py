
from atv_class import Atv


def onetime(filename):
	database = []
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
				if len(myList)<=5:
					myList.append(year)
				else:
					myList.append(year)
					load_atv = Atv(year = myList[0], brand = myList[1], model = myList[2], cc_rating = myList[3], awd = myList[4], price = myList[5])
					database.append(load_atv)
					myList = []
				year = ""
				contence = contence[1:]
	return database
