# Brian Hayes
# 31-Oct-2022

from vehicle_class import Vehicle

class Atv(Vehicle):
	
	def __init__(self, cc_rating, year, model, awd,  brand, price,  classification = "All Terain Vehicle"):

		self.cc_rating 		= cc_rating
		self.classification = classification
		self.year 	= year
		self.model	= model
		self.awd 	= awd
		self.brand 	= brand
		self.price 	= price
		

	def get_cc_rating(self):			return self.cc_rating
	def get_classification(self): 	return self.classification
		
	def get_essence(self):
		aList = [ self.get_classification(),
						self.get_year(),  
						self.get_brand(), 
						self.get_model(), 
						self.get_cc_rating(), 
						self.get_awd(), 
						self.get_price()]
		return aList
	
	def get_essence_as_dict(self):
		a_dict = {"classification" 	: self.classification,
						"year" 					: self.year, 
						"brand" 					: self.brand, 
						"model" 				: self.model, 
						"cc_rating" 			: self.cc_rating, 
						"awd" 					: self.awd, 
						"price" 					: self.price}
		return a_dict
		
		
		
		
		
		
