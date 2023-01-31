# Brian Hayes
#14 Nov 2022

from vehicle_mod import confirm_atv

# IDEAS
# 1) Create a function that when given a list of ATV objects will:
#		1. Return the average price of 
#				a. all atvs sorted by same brand and model
#				b. all atvs sorted by year, model, and brand
# END GOAL
# When a user confirms the information for a new atv, I want to see
# how it compares to the average price of other atvs grouped by year, brand and model,
# and how it compares to other atvs that share the same year, brand, and model.



def get_brand_model_year_averages(atv_object, atv_database):
	
	# This is the cost sum for atvs whos brand, model, and year are the same
	sum_if_same_3 = 0
	# This is the cost sum for atvs whos brand and model are the same
	sum_if_same_2 = 0
	# This is the cost sum for atvs whos brands are the same
	sum_if_same_1 = 0
	
	# This counts how many atvs share the same brand, model, and year
	atvs_in_same_3_catagory = 0
	# This counts how many atvs share the same brand and model
	atvs_in_same_2_catagory = 0
	# This counts how many atvs share the same brand
	atvs_in_same_1_catagory = 0
	
	for atv in atv_database:
		if atv.get_brand() == atv_object.get_brand():
			
			if atv.get_model() == atv_object.get_model():	
				
				if atv.get_year() == atv_object.get_year():

					sum_if_same_3 = sum_if_same_3 + int(atv.get_price())
					sum_if_same_2 = sum_if_same_2 + int(atv.get_price())
					sum_if_same_1 = sum_if_same_1 + int(atv.get_price())
					
					atvs_in_same_3_catagory = atvs_in_same_3_catagory + 1
					atvs_in_same_2_catagory = atvs_in_same_2_catagory + 1
					atvs_in_same_1_catagory = atvs_in_same_1_catagory + 1
				else:
					sum_if_same_2 = sum_if_same_2 + int(atv.get_price())
					sum_if_same_1 = sum_if_same_1 + int(atv.get_price())
					atvs_in_same_2_catagory = atvs_in_same_2_catagory + 1
					atvs_in_same_1_catagory = atvs_in_same_1_catagory + 1
			else:
				sum_if_same_1 = sum_if_same_1 + int(atv.get_price())
				atvs_in_same_1_catagory = atvs_in_same_1_catagory + 1
	
	dict_of_averages = {}
	if sum_if_same_3 != 0:
		the_average_for_same_3 = sum_if_same_3 / atvs_in_same_3_catagory
		dict_of_averages["brand, model, year"] = int(the_average_for_same_3)
	else: dict_of_averages["brand, model, year"] = 0
			
	if sum_if_same_2 != 0:
		the_average_for_same_2 = sum_if_same_2 / atvs_in_same_2_catagory
		dict_of_averages["brand, model"] = int(the_average_for_same_2)
	else: dict_of_averages["brand, model"]  = 0
		
	if sum_if_same_1 != 0:
		the_average_for_same_1 = sum_if_same_1 / atvs_in_same_1_catagory
		dict_of_averages["brand"] = int(the_average_for_same_1)
	else: dict_of_averages["brand"] = 0		
		

					
	return dict_of_averages
					
									
def get_statistic_message(atv_object, atv_database):
	average_info = get_brand_model_year_averages(atv_object, atv_database)
	
	brand_model_year_average = average_info["brand, model, year"]
	brand_model_average = average_info["brand, model"]
	brand_average = average_info["brand"]
	
	if int(atv_object.get_price()) < brand_model_year_average:
		message1 = (" Compared to other ATVs that are the same brand, model, and year, \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_model_year_average))
				+ " less than the average price of $" + str(brand_model_year_average) + "\n")
				
	elif int(atv_object.get_price()) == brand_model_year_average:
		message1 = (" Compared to other ATVs that are the same brand, model, and year, \n"
				+ " your" + confirm_atv(atv_object) + " is the average price." + "\n")

	elif int(atv_object.get_price()) > brand_model_year_average:
		message1 = (" Compared to other ATVs that are the same brand, model, and year, \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_model_year_average))
				+ " more than the average price of $" + str(brand_model_year_average) + "\n")



	if int(atv_object.get_price()) < brand_model_average:
		message2 = ("\n Compared to other ATVs that are the same brand and model \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_model_average))
				+ " less than the average price of $" + str(brand_model_average) + "\n")
		
	elif int(atv_object.get_price()) == brand_model_average:
		message2 = ("\n Compared to other ATVs that are the same brand and model \n"
				+ " your" + confirm_atv(atv_object) + " is the average price." + "\n")

	elif int(atv_object.get_price()) > brand_model_average:
		message2 = ("\n Compared to other ATVs that are the same brand and model \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_model_average))
				+ " more than the average price of $" + str(brand_model_average) + "\n")


	if int(atv_object.get_price()) < brand_average:
		message3 = ("\n Compared to other ATVs that are the same brand \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_average))
				+ " less than the average price of $" + str(brand_average) + "\n")
		
	elif int(atv_object.get_price()) == brand_average:
		message3 = ("\n Compared to other ATVs that are the same brand \n"
				+ " your" + confirm_atv(atv_object) + " is the average price.\n")

	elif int(atv_object.get_price()) > brand_average:
		message3 = ("\n Compared to other ATVs that are the same brand \n"
				+ " your" + confirm_atv(atv_object) + " is \n $" 
				+ str(abs(int(atv_object.get_price()) - brand_average))
				+ " more than the average price of $" + str(brand_average) + "\n")

	message = message1 + message2 + message3

	return message


def get_statistical_data(atv_object, atv_database):
	message = get_statistic_message(atv_object, atv_database)
	return message
























	
