#Brian Hayes
#15 Nov 2022


import unittest

import vehicle_statistic_mod_tests
import main_mod_tests
import auto_fill_mod_tests
import check_functions_tests
import load_and_save_files_tests
import vehicle_tests
import atv_class_tests
import handeling_strings_tests


print("\nRunning atv_class_tests")
suite = unittest.TestLoader().loadTestsFromModule(atv_class_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning atv_statistic_modules_tests")
suite = unittest.TestLoader().loadTestsFromModule(vehicle_statistic_mod_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning main_modules_tests")
print("!! NO TESTS TO RUN!!")
suite = unittest.TestLoader().loadTestsFromModule(main_mod_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning auto_fill_mod_tests")
suite = unittest.TestLoader().loadTestsFromModule(auto_fill_mod_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning check_functions_tests")
suite = unittest.TestLoader().loadTestsFromModule(check_functions_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning load_and_save_files_tests")
suite = unittest.TestLoader().loadTestsFromModule(load_and_save_files_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning working_with_atvs_tests")
suite = unittest.TestLoader().loadTestsFromModule(vehicle_tests)
unittest.TextTestRunner(verbosity=2).run(suite)

print("\nRunning working_with_atvs_tests")
suite = unittest.TestLoader().loadTestsFromModule(handeling_strings_tests)
unittest.TextTestRunner(verbosity=2).run(suite)
