# Brian Hayes
# 28 Apr 2023

import sys
sys.path.append("marketplace/class_files")


from mower_class import Mower
from atv_class import Atv

# MOWERS
t_mower1 = Mower(year="2012", brand="snapper", model="yx42", hp_rating="22", cc_rating="560", price="550",
                    classification="riding mower", deck_size="54", list_date="02 feb 2023", engine_brand="kawasaki")
t_mower2 = Mower(brand="snapper", model="lt1940", hp_rating="20", price="1950", deck_size="50")
t_mower3 = Mower(brand="exmark", model="lazer z", price="2700", deck_size="60", engine_brand="kohler")
t_mower4 = Mower(brand="troybilt", model="bronco", hp_rating="20", deck_size="42", engine_brand="kohler", year="2011", price="350")
t_mower5 = Mower(brand="husqvarna", model="z246", hp_rating="23", engine_brand="briggs and stratton", deck_size="54", price="225")
t_mower6 = Mower(brand="cub cadet", model="ltx1045", hp_rating="20", engine_brand="briggs and stratton", deck_size="42", price="725")
t_mower7 = Mower(brand="country clipper", model="jayz", hp_rating="16", deck_size="54", engine_brand="briggs and stratton", year="2005", price="200")

mower_data = [t_mower1, t_mower2, t_mower3, t_mower4, t_mower5, t_mower6, t_mower7]

# ATVS
t_atv1 = Atv(year = "2000", brand = "yamaha",	model = "sportsman",    cc_rating = "500",	awd = "yes",    price = "2500", 
				classification = "four wheeler", list_date = "02 feb 2023")
t_atv2 = Atv(year = "1997", brand = "yamaha", 	model = "banshee", 		cc_rating = "350", 	awd = "no",     price = "3000", 	classification = "four wheeler")
t_atv3 = Atv(year = "2015", brand = "kawasaki", model = "brute force", 	cc_rating = "750", 	awd = "yes",    price = "4250", 	classification = "four wheeler")
t_atv4 = Atv(year = "2012", brand = "polaris", 	model = "sportsman", 	cc_rating = "400", 	awd = "yes", 	price = "400", 		classification = "four wheeler")
t_atv5 = Atv(year = "2002", brand = "polaris", 	model = "sportsman", 	cc_rating = "500", 	awd = "yes", 	price = "2800", 	classification = "four wheeler")
t_atv6 = Atv(year = "1998", brand = "polaris", 	model = "xplorer", 		cc_rating = "400", 	awd = "yes", 	price = "1800", 	classification = "four wheeler")
t_atv7 = Atv(year = "1987", brand = "honda", 	model = "fourtrax", 	cc_rating = "350", 	awd = "yes", 	price = "600", 		classification = "four wheeler")
t_atv8 = Atv(year = "1996", brand = "polaris", 	model = "sportsman", 	cc_rating = "350", 	awd = "no", 	price = "100", 		classification = "four wheeler")
t_atv9 = Atv(year = "2000", brand = "polaris", 	model = "sportsman", 	cc_rating = "1000", awd = "no", 	price = "2000", 	classification = "four wheeler")
t_atv10 = Atv(year = "2022", brand = "polaris", model = "sportsman", 	cc_rating = "500", 	awd = "yes", 	price = "1350", 	classification = "four wheeler")
t_atv11 = Atv(year = "2018", brand = "polaris", model = "xplorer", 		cc_rating = "400", 	awd = "yes", 	price = "1600", 	classification = "four wheeler")
t_atv12 = Atv(year = "2009", brand = "honda", 	model = "fourtrax", 	cc_rating = "350", 	awd = "yes", 	price = "600", 		classification = "four wheeler")
t_atv13 = Atv(year = "2004", brand = "polaris", model = "sportsman", 	cc_rating = "350", 	awd = "no", 	price = "400", 		classification = "four wheeler")
t_atv14 = Atv(year = "2012", brand = "polaris", model = "sportsman", 	cc_rating = "1000", awd = "no", 	price = "450", 		classification = "four wheeler")
t_atv15 = Atv(year = "2012", brand = "honda", 	model = "ex", 			cc_rating = "400", 	awd = "no", 	price = "2500", 	classification = "four wheeler")

atv_data = [t_atv1, t_atv2, t_atv3, t_atv4, t_atv5, t_atv6, t_atv7, t_atv8, t_atv9, t_atv10, t_atv11, t_atv12,
            t_atv13, t_atv14, t_atv15]


# REAL FBM DESCRIPTIONS OF ITEMS
# LISTS FOR AUTO_FILL
# Mowers

list1 = ["225", "riding", "mower", "shop", "vac", "goshen", "ky","cub","cadet", "riding", "mower", "needs",
         "tlc", "replaced", "spindles", "two", "years", "ago", "needs", "belt", "n", "battery", "225", "obo",
         "little", "shop", "vac", "for", "smaller", "projects", "8"]
list2 = ["1825", "west", "harrison", "in", "husqvarna", "zero", "turn", "mower", "54", "inch", "cut", "54",
         "inch", "cut", "23hp", "briggs", "engine", "rums", "and", "cuts", "great", "ready", "to", "mow", "tags",
         "john", "deere", "ferris", "kubota", "bobcat", "troybilt", "pony", "horse", "great", "dane", "toro",
         "simplicity", "citation", "hustler", "proline", "titan", "myride", "21", "42", "46", "48", "52", "60",
         "61", "72", "is", "21hp", "kawasaki", "fx", "fh", "fr", "z3", "z2", "z1", "country", "clipper", "redmax",
         "dewalt", "snap", "on", "bushhog", "cub", "cadet", "xt1", "xt2", "xt3", "alpha", "tiger", "woods", "altoz",
         "is2100", "is3200", "stihl", "echo", "leaves", "pro", "z",  "patriot", "freedom", "z", "liberty",  "x300",
         "x500", "ariens", "ikon", "edge", "toro", "z515", "snapper", "z", "master", "skag", "scagg", "gravely",
         "dingo", "mt", "bobcat", "mt55", "mt85"]
list3 = ["200", "pending", "2005", "country", "clipper", "jayz", "versailles", "in", "54", "inch", "country", 
         "clipper", "motor", "blown"]
list4 = ["1500", "john", "deere", "7", "iron", "commercial", "mower", "26hp", "kohler", "command", "new", 
         "tired", "and", "fresh", "blades", "48", "deck", "shelbyville", "in", "this", "is", "a", "second", 
         "mower", "we", "use", "if", "we", "need", "too", "serviced", "over", "the", "winter", "have", "used", 
         "it", "the", "past", "few", "weeks", "with", "our", "ferris", "down", "not", "interested", "in", 
         "offers", "its", "not", "costing", "me", "to", "keep", "it", "not", "sure", "on", "hours"]

auto_fill_list = [list1, list2, list3, list4]