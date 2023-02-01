#Brian Hayes
# 01 Feb 2023

class Item (object):
	
		def __init__ (self, brand, price):
			
			self.brand 	= brand
			self.price 	= price
			
		def get_price(self):			return self.price
		def get_brand(self):		return self.brand
