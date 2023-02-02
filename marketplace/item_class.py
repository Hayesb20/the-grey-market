#Brian Hayes
# 01 Feb 2023
from datetime import datetime


class Item (object):
	
		def __init__ (self, **kwargs):
			
			self.brand 	= kwargs["brand"]
			self.price 	= kwargs ["price"]
			try: self.date		= kwargs["date"]
			except: self.date = datetime.now()
			
		def get_price(self):				return self.price
		def get_brand(self):			return self.brand
		def get_date_listed(self): 	return self.date.strftime("%d %b %Y")
