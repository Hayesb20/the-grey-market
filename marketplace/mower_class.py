# Brian Hayes
# 01 Jan 2023

class Mower():
	
	def __init__(self, brand, hp_rating, deck_size, classification, price, model="N/A"):
		
		self.brand 					= brand
		self.model 				= model
		self.hp_rating 			= hp_rating
		self.deck_size 			= deck_size
		self.classification 	= classification
		self.price 					= price
		
		
	def get_brand(self): 				return self.brand
	def get_model(self): 				return self.model
	def get_hp_rating(self):			return self.hp_rating
	def get_deck_size(self): 		return self.deck_size
	def get_classification(self): 	return self.classification
	def get_price(self): 				return self.price


		
	def get_essence(self):
		aList = [self.brand, self.model, self.hp_rating, self.deck_size,
						self.classification, self.price]
		return aList
