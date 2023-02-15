#Brian Hayes
# 01 Feb 2023
from datetime import datetime


class Item (object):
	
		def __init__ (self, **kwargs):
			
			# All arguments are strings
			self.brand 	= kwargs["brand"].strip().lower()																		
			self.price 	= kwargs ["price"].replace(" ","")																			
			try: self.list_date		= kwargs["list_date"]
			except: self.list_date 	= datetime.strftime(datetime.now(),"%d %b %Y")
			
		def get_price(self):				return self.price
		def get_brand(self):			return self.brand
		def get_list_date(self): 		return self.list_date.title()
