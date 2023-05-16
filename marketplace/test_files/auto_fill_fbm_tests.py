# Brian Hayes
# 28 Apr 2023

import sys
sys.path.append("marketplace/modules")
sys.path.append("marketplace/class_files")

import unittest
import auto_fill_mod as mod
from test_database import auto_fill_list, mower_data


class Auto_Fill_With_FBM_Strings(unittest.TestCase):
    # This class is meant to test the capabilities of autofill
    # with real world user comments and descriptions of items
    # from FaceBook Marketplace (FMB).

    def est_autofill_mower_input_1(self):
        # This test will use input gathered from a mower listing
        user_list = auto_fill_list[0] # Using list1
        expected_dict = {"brand":"cub cadet",
                         "price":"225"}
        autofilled_dict = mod.autofill_vehicle(user_list, mower_data)

        self.assertEqual(expected_dict, autofilled_dict)

    def test_autofill_mower_input_2(self):
        # This test will use input gathered from a mower listing
        user_list = auto_fill_list[1] # Using list 2
        expected_dict = {"brand":"husqvarna",
                         "hp_rating":"23", 
                         "price":"1825",
                         "deck_size":"54", 
                         "engine_brand":"briggs"
                         }
        autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
        self.assertEqual(expected_dict, autofilled_dict)

    def est_autofill_mower_input_3(self):
        # This test will use input gathered from a mower listing
        user_list = auto_fill_list[2] # Using list 3
        expected_dict = {"brand":"country clipper",
                         "model":"jayz", 
                         "price":"200",
                         "deck_size":"54",
                         "year":"2005"
                         }
        autofilled_dict = mod.autofill_vehicle(user_list, mower_data)
        self.assertEqual(expected_dict, autofilled_dict)







if __name__ == '__main__':
    unittest.main()