# Brian Hayes
# 03 Feb 2023

from vehicle_class import Vehicle as V

class Mower(V):
	
	def __init__(self, **kwargs):
		V.__init__(self, **kwargs)
		
		# Required args that can be a default values
		try: self.deck_size = kwargs["deck_size"]
		except: self.deck_size = "unknown"
	
		try: self.cc_rating = kwargs["cc_rating"]
		except: self.cc_rating = "unknown"
		
		try: self.hp_rating = kwargs["hp_rating"]
		except: self.hp_rating = "unknown"
		
		try: self.classification = kwargs["classification"].lower()
		except: self.classification = "mower"
		
		try: self.engine_brand = kwargs["engine_brand"].lower()
		except: self.engine_brand = "unknown"

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
						
		if self.get_cc_rating() != "unknown"			: aList.append(self.get_cc_rating()) 		# mower_class
		if self.get_hp_rating() != "unknown"			: aList.append(self.get_hp_rating()) 		# mower_class
		if self.get_engine_brand() != "unknown"	: aList.append(self.get_engine_brand())	# mower_class
		if self.get_year() != "unknown"					: aList.append(self.get_year())					# vehicle_class
		
		return aList
	
	# A dictionary of attributes
	def get_essence_as_dict(self):
		a_dict = {"classification" 	: self.get_classification(),
						"brand" 					: self.get_brand(), 
						"model" 				: self.get_model(), 
						"deck_size"			: self.get_deck_size(),
						"price" 					: self.get_price(),
						"list date"				: self.get_list_date()}
						
		if self.get_hp_rating() != "unknown"			: a_dict["hp_rating"]		 	= self.get_hp_rating() 		# mower_class
		if self.get_cc_rating() != "unknown"			: a_dict["cc_rating"] 		 	= self.get_cc_rating()			# mower_class
		if self.get_engine_brand() != "unknown"	: a_dict["engine_brand"] 	= self.get_engine_brand()	# mowre_class
		if self.get_year() != "unknown"					: a_dict["year"]					= self.get_year()					# vehicle_class
		
		return a_dict



















