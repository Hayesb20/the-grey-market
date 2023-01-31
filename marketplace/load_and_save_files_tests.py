# Brian Hayes
#16 Nov 2022

import unittest
import load_and_save_files as LaS


class Save_File(unittest.TestCase):
	def test_save_file_1(self):
		database1 = {"yamaha" : ["banshee"]}
		filename = "txt_files/brands_and_models.txt"
		LaS.save_file(database1, filename)



if __name__ == '__main__':
    unittest.main()
