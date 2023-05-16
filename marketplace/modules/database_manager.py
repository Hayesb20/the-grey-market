# Brian Hayes
# 27 Apr 2023

from user import user_info

# Database_Manager is the central control moduel for making any changes to any database
# in the grey market program. No file should manipulate data inside of a file that is a
# database without accessing it through Database_Manager. No code should access 
# load_and_save_files except Database_Manager

# Database_Manager should be able to:
#   !! The predetermined location should be a filepath hardcoded in to represent where the 
#       user would like all the data to be kept !! -- Someday might make this location part 
#       of a setup file --
# Create new files that represent databases in a predetermined local driver location.
# Delete files that reprsent databases in a predeterminded local driver location
# Add item/s (objects) to a specific database
# Delete specific item/s to a specific database
# Determin if an item can be located in a specific database
# Determin if an item can be located in any database
# Load contense of a database
# Save a current version of a database
# Have a backup copy of each database. The backup can be loaded/overwritten when needed


class Database_Manager(user_info["filep_to_databases"]):
    pass