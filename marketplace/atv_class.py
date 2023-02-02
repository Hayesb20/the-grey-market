# Brian Hayes
# 31-Oct-2022

from vehicle_class import Vehicle as V

class Atv(V):
	
	def __init__(self, **kwargs):
		V.__init__(self, **kwargs)

		# Required argument
		self.cc_rating = kwargs["cc_rating"]
		self.awd 	= kwargs ["awd"]
		# Required arg that can be a default value
		try: self.classification = kwargs["classification"]
		except: self.classification = "All Terain Vehicle"
		

	def get_cc_rating(self):			return self.cc_rating
	def get_classification(self): 	return self.classification
	def get_awd(self):					return self.awd
		
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
		
		
		
		
		
		
