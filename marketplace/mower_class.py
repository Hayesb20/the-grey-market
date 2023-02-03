# Brian Hayes
# 03 Feb 2023

from vehicle_class import Vehicle as V

class Mower(V):
	
	def __init__(self, **kwargs):
		V.__init__(self, **kwargs)
		
		# Required args
		self.deck_size = kwargs["deck_size"]
		
		# Required args that can be a default values
		try: self.cc_rating = kwargs["cc_rating"]
		except: self.cc_rating = "Unknown"
		
		try: self.hp_rating = kwargs["hp_rating"]
		except: self.hp_rating = "Unknown"
		
		try: self.classification = kwargs["classification"]
		except: self.classification = "Mower"
		
		try: self.engine_brand = kwargs["engine_brand"]
		except: self.engine_brand = "Unknown"

	# Get functions
	def get_classification(self): 	return self.classification
	def get_cc_rating(self):			return self.cc_rating
	def get_hp_rating(self):			return self.hp_rating
	def get_deck_size(self):			return self.deck_size
	def get_engine_brand(self):	return self.engine_brand

	# An unordered list of attributes of the object
	def get_essence(self):
		aList = [ self.get_classification(), # mower_class
						self.get_brand(), 				# item_class
						self.get_model(), 				# vehicle_class
						self.get_deck_size(),		# mower_class
						self.get_price(),				# item_class
						self.get_list_date()]			# item_class
						
		if self.get_cc_rating() != "Unknown"			: aList.append(self.get_cc_rating()) 		# mower_class
		if self.get_hp_rating() != "Unknown"			: aList.append(self.get_hp_rating()) 		# mower_class
		if self.get_engine_brand() != "Unknown"	: aList.append(self.get_engine_brand())	# mower_class
		if self.get_year() != "Unknown"					: aList.append(self.get_year())					# vehicle_class
		
		return aList
	
	# A dictionary of attributes
	def get_essence_as_dict(self):
		a_dict = {"classification" 	: self.get_classification(),
						"brand" 					: self.get_brand(), 
						"model" 				: self.get_model(), 
						"deck_size"			: self.get_deck_size(),
						"price" 					: self.get_price(),
						"list date"				: self.get_list_date()}
						
		if self.get_hp_rating() != "Unknown"			: a_dict["hp_rating"]		 	= self.get_hp_rating() 		# mower_class
		if self.get_cc_rating() != "Unknown"			: a_dict["cc_rating"] 		 	= self.get_cc_rating()			# mower_class
		if self.get_engine_brand() != "Unknown"	: a_dict["engine_brand"] 	= self.get_engine_brand()	# mowre_class
		if self.get_year() != "Unknown"					: a_dict["year"]					= self.get_year()					# vehicle_class
		
		return a_dict



















