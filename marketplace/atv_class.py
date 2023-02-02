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
						self.get_price(),
						self.get_list_date()]
		return aList
	
	def get_essence_as_dict(self):
		a_dict = {"classification" 	: self.get_classification(),
						"year" 					: self.get_year(), 
						"brand" 					: self.get_brand(), 
						"model" 				: self.get_model(), 
						"cc_rating" 			: self.get_cc_rating(), 
						"awd" 					: self.get_awd(), 
						"price" 					: self.get_price(),
						"list date"				: self.get_list_date()}
		return a_dict
		
		
		
		
		
		
