#Brian Hayes
#15 Nov 2022

import sys
sys.path.append("marketplace/test_files")

# External Imports
import unittest

# Class tests
import mower_class_tests
import atv_class_tests
import item_class_tests

# Misc Tests
import vehicle_statistic_mod_tests
import auto_fill_atv_tests
import auto_fill_mower_tests
import check_functions_tests
import load_and_save_files_tests
import handeling_strings_tests
import vehicle_mod_tests
import auto_fill_fbm_tests


print("\nRunning item_class_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(item_class_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning mower_class_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(mower_class_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning atv_class_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(atv_class_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning vehicle_mod_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(vehicle_mod_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning atv_statistic_modules_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(vehicle_statistic_mod_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning auto_fill_mod_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(auto_fill_atv_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning auto_fill_mod_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(auto_fill_mower_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning check_functions_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(check_functions_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning load_and_save_files_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(load_and_save_files_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning working_with_atvs_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(handeling_strings_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning auto_fill_fbm_tests.py")
suite = unittest.TestLoader().loadTestsFromModule(auto_fill_fbm_tests)
unittest.TextTestRunner(verbosity=2).run(suite)
