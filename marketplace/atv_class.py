# Brian Hayes
# 31-Oct-2022

#this class needs to inharit from another class so i can add a "type" to this which lets me know 
#that objects from this are atv objects

class Atv():
	
	def __init__(self, year, brand, model, cc_rating, awd, price):
		self.year 			= year
		self.model			= model
		self.cc_rating 	= cc_rating
		self.price 			= price
		self.brand 			= brand
		self.awd 			= awd
		
	def get_year(self): 			return self.year
	def get_model(self):		return self.model
	def get_cc_rating(self):	return self.cc_rating
	def get_price(self):			return self.price
	def get_brand(self):		return self.brand
	def get_awd(self):			return self.awd
		
	def get_essence(self):
		aList = [ self.year,  
						self.brand, 
						self.model, 
						self.cc_rating, 
						self.awd, 
						self.price]
		return aList
	def get_essence_as_dict(self):
		a_dict = {"year" 			: self.year, 
						"brand" 			: self.brand, 
						"model" 		: self.model, 
						"cc_rating" 	: self.cc_rating, 
						"awd" 			: self.awd, 
						"price" 			: self.price}
		return a_dict
		
		
		
		
		
		
