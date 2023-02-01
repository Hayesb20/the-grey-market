# Brian Hayes
# 02 Feb 2023

from item_class import Item


class Vehicle(Item):
	
	def __init__ (self, year, model, awd,  brand, price):
		
		self.year 	= year
		self.model	= model
		self.awd 	= awd
		
	def get_year(self): 			return self.year
	def get_model(self):		return self.model
	def get_awd(self):			return self.awd
	
