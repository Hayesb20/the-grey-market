# Brian Hayes
# 02 Feb 2023

from item_class import Item as I


class Vehicle(I):
	
	def __init__ (self, **kwargs):
		I.__init__(self, **kwargs)
		
		try: self.year 	= kwargs["year"]
		except: self.year 	= "Unknown"
			
		self.model	= kwargs["model"]
		
		
	def get_year(self): 			return self.year
	def get_model(self):		return self.model

	
