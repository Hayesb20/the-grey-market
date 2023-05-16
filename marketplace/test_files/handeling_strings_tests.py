# Brian Hayes
# 23 Jan 2023
import sys
sys.path.append("marketplace/modules")


import unittest
import handeling_strings as HS

class Parse(unittest.TestCase):
	
	
	# Input: Consists of upper & lower case characterts
	# Exprectation: Returns a list of each word with all lowercase characters
	def test_parse_1(self): 
		string = "2009 Polaris Sportsman 350 no 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		a_list = HS.parse(string)
		self.assertEqual(expected_list, HS.parse(string))
		
	# Input: Consists of all upper case characterts
	# Exprectation: Returns a list of each word with all lowercase characters
	def test_parse_2(self): 
		string = "2009 POLARIS SPORTSMAN 350 NO 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		a_list = HS.parse(string)
		self.assertEqual(expected_list, HS.parse(string))
		
	# Input: Consists of all lower case characterts
	# Exprectation: Returns a list of each word with all lowercase characters
	def test_parse_3(self): 
		string = "2009 polaris sportsman 350 no 3000"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		self.assertEqual(expected_list, HS.parse(string))
	
	# Input: Contains non-digit and non-alphabetic characters 
	# Expectation: Returns a list of each word without any non-alphanumeric notation
	def test_parse_4(self): 
		string = "20-09 $polaris sportsman! @$350 *no (3000%)"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		self.assertEqual(expected_list, HS.parse(string))

	# Input: Input string contains multiple white spaces between words
	# Expectation: Returns a list of each word without any white spaces
	def test_parse_5(self): 
		string = "   2009  polaris       sportsman 350 no    3000   )"
		expected_list = ["2009", "polaris", "sportsman", "350", "no", "3000"]
		self.assertEqual(expected_list, HS.parse(string))
		
	def test_parse_with_live_fbm_comments1(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("$350 42 inch cut Troy-Bilt Bronco 20 horsepower Kohler Have a nice 2011"
		 	+ " Troy-Bilt Bronco with a 20 horse Kohler runs and cuts great I would like"
			+ " to trade for very quiet nice generator can deliver for a small fee I have"
			+ " a video of it running")
		expected_list = ["350", "42", "inch", "cut", "troybilt", "bronco", "20", "horsepower",
		     "kohler", "have", "a", "nice", "2011", "troybilt", "bronco", "with", "a",
			  "20", "horse", "kohler", "runs", "and", "cuts", "great", "i", "would", "like",
			"to", "trade", "for", "very", "quiet", "nice", "generator", "can", "deliver", 
			"for", "a", "small", "fee", "i", "have", "a", "video", "of", "it", "running"]

		self.assertEqual(expected_list, HS.parse(string))

	def test_parse_with_live_fbm_comments2(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("1,825 West Harrison, IN Husqvarna Zero Turn Mower 54 Inch Cut !!@@@ 54 inch cut "
	    	+"23hp Briggs engine Rums and cuts great Ready to mow Tags; John deere ferris Kubota "
			+"bobcat troybilt pony horse great Dane toro simplicity citation hustler proline titan "
			+"myride 21 42 46 48 52 60 61 72 is 21hp kawasaki fx fh fr z3 z2 z1 country clipper " 
			+"redmax Dewalt snap on bushhog cub cadet xt1 xt2 xt3 alpha tiger woods altoz Is2100 " 
			+"is3200 stihl echo leaves pro z  patriot freedom z liberty  x300 x500 Ariens ikon edge " 
			+"toro z515 snapper z master skag scagg gravely  dingo Mt bobcat mt55 mt85")
		expected_list = ["1825", "west", "harrison", "in", "husqvarna", "zero", "turn", "mower", "54", "inch", "cut", "54",
         "inch", "cut", "23hp", "briggs", "engine", "rums", "and", "cuts", "great", "ready", "to", "mow", "tags",
         "john", "deere", "ferris", "kubota", "bobcat", "troybilt", "pony", "horse", "great", "dane", "toro",
         "simplicity", "citation", "hustler", "proline", "titan", "myride", "21", "42", "46", "48", "52", "60",
         "61", "72", "is", "21hp", "kawasaki", "fx", "fh", "fr", "z3", "z2", "z1", "country", "clipper", "redmax",
         "dewalt", "snap", "on", "bushhog", "cub", "cadet", "xt1", "xt2", "xt3", "alpha", "tiger", "woods", "altoz",
         "is2100", "is3200", "stihl", "echo", "leaves", "pro", "z",  "patriot", "freedom", "z", "liberty",  "x300",
         "x500", "ariens", "ikon", "edge", "toro", "z515", "snapper", "z", "master", "skag", "scagg", "gravely",
         "dingo", "mt", "bobcat", "mt55", "mt85"]

		self.assertEqual(expected_list, HS.parse(string))
		
	def test_parse_with_live_fbm_comments3(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("$950 Cub Cadet Zero Turn Mower 48 Shirley, IN 48” deck cub cadet ztr. Runs and mowes fine. 22 " 
	    		+ "hp Briggs and Stratton. Had it for years and got a new one. $950.00 obo Shirley in "
				+ "[hidden information]")
		
		expected_list = ["950", "cub", "cadet", "zero", "turn", "mower", "48", "shirley", "in", "48", "deck", "cub",
		   				"cadet", "ztr", "runs", "and", "mowes", "fine", "22", "hp", "briggs", "and", "stratton", 
						"had", "it", "for", "years", "and", "got", "a", "new", "one", "950", "obo", 
						"shirley", "in", "hidden", "information"]

		self.assertEqual(expected_list, HS.parse(string))

	def test_parse_with_live_fbm_comments4(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("$2,400 John Deere Zero Turn Mower 42” Z345R Only 50 hours! 22hp. 42” deck."
	    		+ " Many extras. Hitch and bumper. Mulching kit. Wired for sprayer")
		
		expected_list = ["2400", "john", "deere", "zero", "turn", "mower", "42", "z345r", 
		   				"only", "50", "hours", "22hp", "42", "deck", "many", "extras", 
						"hitch", "and", "bumper", "mulching", "kit", "wired", "for", "sprayer"]
		self.assertEqual(expected_list, HS.parse(string))		
		
	def test_parse_with_live_fbm_comments5(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("$1,500 john deere 7 iron commercial mower.26hp kohler command new tired "
	    		+ 'and fresh blades.48" deck Shelbyville, IN This is a second mower we use '
				+ "if we need too.serviced over the winter have used it the past few weeks "
				+ "with our ferris down.not interested in offers it's not costing me to keep "
				+ " it not sure on hours")
		
		expected_list = ["1500", "john", "deere", "7", "iron", "commercial", "mower", "26hp",
		   				"kohler", "command", "new", "tired", "and", "fresh", "blades", "48",
						"deck", "shelbyville", "in", "this", "is", "a", "second", "mower", 
						"we", "use", "if", "we", "need", "too", "serviced", "over", "the", 
						"winter", "have", "used", "it", "the", "past", "few", "weeks", "with",
						"our", "ferris", "down", "not", "interested", "in", "offers", "its",
						"not", "costing", "me", "to", "keep", "it", "not", "sure", "on", "hours"]
		
		self.assertEqual(expected_list, HS.parse(string))	

	def test_parse_with_live_fbm_comments6(self):
		self.maxDiff = None
		# parse should create a list of each full word/number in the comment. Each word will be
		# in all lowercase
		string = ("$200 Pending  · 2005 Country clipper jay-z  Versailles,"
	    		+ " IN 54 inch country clipper motor blown ")
		
		expected_list = ["200", "pending", "2005", "country", "clipper", "jayz", "versailles",
		   		 "in", "54", "inch", "country", "clipper", "motor", "blown"]
		
		self.assertEqual(expected_list, HS.parse(string))








if __name__ == '__main__':
    unittest.main()
	
