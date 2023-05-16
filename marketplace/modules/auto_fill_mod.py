import datetime
import regex as re

# Autofill will recieve a "users_list" which is a list of strings. These strings represent
# the information needed to make a vehicle. This could be information to make any classification
# of vehicle.

# Autofill will also recieve a "database" which is a list of all vehicle objects that the system 
# knows about. This database may be empty.

# Autofill will return a dictionary with key value pairs. The keys will be strings like but not
# limited to "brand" "model" "year" etc. The values will be appropriate strings from the 
# "users_list". These key/value pairs will be used as the kwargs for making vehicle objects.
# UPDATE autofill should be able to work with any kind of item

# --GOAL--
# This function should consider each string on an individual basis as well as a collection to determin
# what string (value) should be associated with which key 
# The returned dictionary should have as many of the strings confidently placed with the correct key
# as possible

# Thoughts
# May try to have 1 function dedicated to looking for a respective key. A function dedicated to finding the
# most appropriate value for the year if any exist.
# Once all functions have found suitable values, if possible with the given strings, maybe try to have a 
# function that recognizes functions that have claimed the same value and make a desicion between them. 
# Possibly when all values seem feasable, try to discover which vehicle the user is trying to make so that
# you can get an idea as to what key/values we should expect


def is_likely_a_year(curr_string, users_list):
    # This function recieves a string that is a digit and helps to determin 
    # whether or not that string is likely to be the number represening a 
    # year given a set of rules
    # Rule 1 - There are only 3 numbers to date (2023) where the year is 
    #           divisable by 25 with a remainder of 0. Thus, if the string
    #           is divisable by 25 with a remainder of 0 we will assume that
    #           it is not a year. Those years are 1950, 1975, and 2000
    # Rule 2 - We are only considering years between 1950 and the current year
    #           plus 1. So if the string falls without that range, it is not a year


    if (int(curr_string)%25 == 0     # if the number is divisable by 25 with a remainder of not 0
        or int(curr_string) < 1950   # or the number is less than 1950
        or int(curr_string) > 2024): # or the number is larger than 2024
        return False            # The number is likely a year
    elif dup_numbers(curr_string, users_list) == True:
        return False # The number is likely a year
    
    return True # Otherwise the number is unlikely to be a year

def new_is_more_likely(string, a_dict, curr_best, users_list):
    # This function is ment to determin which number is most likely to be
    # the price by checking them against a series of rules and guides
    # Rule 1 - If one number is within the range for engine power and the other
    # is larger than that range, the larger is more liekly to be the price
    # Rule 2 - If the the "year" has already been filled and this new number is
    # equal to that year, and it is not duplicate number, the new number is not
    # likely to be the price.
    #if int(string) > 1000 and int(curr_best) <= 1000: return False
    #print("string", string)
    if ("year" in a_dict and int(string) == int(a_dict["year"]) 
        and dup_numbers(string, a_dict) == True): return False
    if ("year" in a_dict and int(string) == int(a_dict["year"])): return False
    for key in a_dict:
        if (a_dict[key] == curr_best and dup_numbers(string, users_list) == True): 
            return True
    if int(string) < int(curr_best): return False
    return True
    
   

def dup_numbers(string, users_list):
    # This function will take a string and a list and then return True
    # if that string appears more than once in that list
    counter = 0
    for a_str in users_list:
        if string == a_str: counter = counter + 1
    if counter >= 2: return True
    else: return False

def find_price(users_list, database, a_dict):
    # The price can be any number >= 0
    # Prices are usually devisable by 5 with a remainder of 0
    #   This is only true for items listed in places like ebay or facebook
    # Prices for a type of item will follow a trend but the price could be an outliar
    # Numbers that follow the x.xx pattern should be assumed to be the prices
    # There may also be instances where there are multiple str that match prices of things
    # in the database. 

    model_price_acc = 0
    model_count_acc = 0
    list_of_model_cc_n_hp_rate = []

    brand_price_acc = 0
    brand_count_acc = 0 
    for item in database:
       # if we can determin a brand and/or model we can narrow the search
       # and get more accurate data faster
        try:
            if a_dict["model"] == item.get_model():
                model_price_acc = model_price_acc + int(item.get_price())
                model_count_acc = model_count_acc + 1
                if item.get_cc_rating() != "unknown":
                    list_of_model_cc_n_hp_rate.append(item.get_cc_rating())
                if item.get_hp_rating() != "unknown":
                    list_of_model_cc_n_hp_rate.append(item.get_hp_rating())
        except: pass
        try:
            #print("a ict",a_dict["brand"])
            if a_dict["brand"] == item.get_brand():
                brand_price_acc = brand_price_acc + int(item.get_price())
                brand_count_acc = brand_count_acc + 1
                if item.get_cc_rating() != "unknown":
                    list_of_model_cc_n_hp_rate.append(item.get_cc_rating())
                if item.get_hp_rating() != "unknown":
                    list_of_model_cc_n_hp_rate.append(item.get_hp_rating())
                
                #print("brands count in loop", brand_count_acc)
        except: pass
        
    #print("the hp/cc thing after the try", list_of_model_cc_n_hp_rate)
    if model_count_acc != 0:
        count_acc = model_count_acc
        price_acc = model_price_acc
    else:
        #print("brand count in else", brand_count_acc)
        count_acc = brand_count_acc
        price_acc = brand_price_acc
        #print("the count",count_acc)
    #print(model_count_acc)
    
    if count_acc == 0: return
    average_price = price_acc/count_acc
    #print("the average price is", average_price)
    best_match = None
    for str in users_list:
        if str.isdigit():  
            if model_count_acc != 0 or brand_count_acc != 0:
                if (str not in list_of_model_cc_n_hp_rate
                    or dup_numbers(str, users_list) == True):
                    if best_match == None and is_likely_a_year(str, users_list) == False:
                        best_match = str
                        #print("best match was none but is now ", best_match)
                    else:
                        if best_match != None:
                            #print("this is str", str)
                            if (abs(abs(int(best_match))-abs(int(average_price))) > abs(abs(int(str)-abs(int(average_price)))) 
                                or new_is_more_likely(str, a_dict, best_match, users_list) == True
                                or some_foo(str, users_list, a_dict) == True):
                                #print("T OR F", is_there_bigger_num_not_year(str, users_list, best_match))
                                if (is_there_bigger_num_not_year(str, users_list, best_match) == True
                                    and new_is_more_likely(str, a_dict, best_match, users_list) == False): 
                                    best_match = str
                                    #print("if 1 we changed new best to be ",best_match)

                                if (is_there_bigger_num_not_year(str, users_list, best_match) == False
                                    and new_is_more_likely(str, a_dict, best_match, users_list) == True): 
                                    best_match = str
                                    #print("if 1.1 we changed new best to be ",best_match)

                                if (is_there_bigger_num_not_year(str, users_list, best_match) == True
                                    and some_foo(str, users_list, a_dict) == True): 
                                    best_match = str
                                    #print("if 2 we changed new best to be ",best_match)
                                    
                                if (is_there_bigger_num_not_year(str, users_list, best_match) == False
                                    and is_likely_a_year(str, users_list) == False
                                    and new_is_more_likely(str, a_dict, best_match, users_list) == True):
                                    best_match = str
                                    #print("if 3 we changed new best to be ",best_match)
                
    # Intended to catch scenarios where the price is found within the list
    # of cc_ratings and hp_ratings
    if best_match == None:
        eps_and_price = []
        for string in users_list:
            if string.isdigit():
                if int(string) <= 1000:
                    eps_and_price.append(string)
        
        #print("before", eps_and_price)
        for string in eps_and_price:
            dict_keys = a_dict.keys()
            for key in dict_keys:
                if key == "cc_rating":
                    if string == a_dict[key]:
                        eps_and_price.remove(string)
                if key == "hp_rating":
                    if string == a_dict[key]:
                        eps_and_price.remove(string)
        #print("after", eps_and_price)
        if len(eps_and_price) == 1: best_match = eps_and_price[0]

    #print(best_match)      
    return best_match

def some_foo(str, users_list, a_dict):
    #print("str", str)
    
    if ("year" in a_dict # If the year key already exists in a_dict
        and dup_numbers(str, users_list) == True # If there are duplicate numbers in users_list
        and is_there_bigger_num_not_year(str, users_list) == True): # If there is NOT a larger number thats not a year
        #print("retunring true in foo")
        return True

def is_there_bigger_num_not_year(str, users_list, best_match=0):
    #print("the str here 1 ", str, best_match)
    for string in users_list:
        if string.isdigit():
            if (int(string) > int(str)                              # If string is larger than str
                and int(str) > int(best_match)                      # or str is less than best match
                and is_likely_a_year(string, users_list) == True):  # and string is not likely a year
                #print("its me")
                return False                                        # Then string is larger than str and not a year
            elif (int(string) > int(str)                            # If there is a string in the list that is larger than str
                and int(str) > int(best_match)
                and is_likely_a_year(string, users_list) == False): # and that string is not likely a year
                return True  
                
            else : 
                #print("its me2")
                return False                                      # Then str is not the largest number that is not a year
    return True

def find_year(users_list, database, a_dict):
    # The year can only be between 1950 and the present year + 1
        # I have no interest in vehicles older than 1950 at the moment
    # Edge cases
        # 1) The database might not have any vehicles that match the brand and year
        # 2) The users list might not contain a year
        # 3) There may be multiple numbers that could be applicable years. In particual the price
        #   However it should be safe to assume that the price will be in an incrament of 5
    times_occured = 0
    list_of_pos_years = []
    best_match = ""
    for str in users_list:
        if str.isdigit():
            if int(str) >= 1950 and int(str) <= (1+int(datetime.datetime.now().year)):
                times_occured = times_occured + 1
                list_of_pos_years.append(str)
                best_match = str

    #print("times ",times_occured)
    if times_occured == 0: return
    elif times_occured == 1: return best_match
    elif times_occured == 2:
        if dup_numbers(best_match, users_list): return best_match
        else:
            for str in list_of_pos_years:
                if is_likely_a_year(str, users_list):
                    return str #str is the best match and also will be the first match it finds
    else: pass # There are more than 1 option for year. Need to identify best option
                
def find_EP (users_list, database, a_dict):
    # This function must return a key and a value
        # The first value to be returned will be the key "hp" or "cc"
        # The second will be the number
    # Users list may not contain an appropriate value
    # The value may be in CC or HP mesurement
    # There may not be a power value supplied
    # The value, regardless of it being denoted as HP or CC will be less that 1000
        # Things denoted as CC are usually converted into the HP notation before
        # crossing the 1000 threshold
        # Exceedingly few items cross the 1000hp threshold

    # Checks for any strings in the users_list that appear like "20hp" or "400cc" as those are 
    # the obvious values for the Engine power raiting and its denotation
    for string in users_list:
        if re.match("[0-9]*hp", string):
            denotation = "hp_rating"
            ep = re.match("[0-9]*", string)
            return denotation, ep.group(0)

        elif re.match("[0-9]*cc", string):
            denotation = "cc_rating"
            ep = re.match("[0-9]*", string)
            return denotation, ep.group(0)


    denotation = get_denotation(database, a_dict)
    count_occurances = 0
    viable_options = []
    best_match = "0"
    for a_str in users_list:
        if a_str.isdigit():
            if int(a_str) < 1000:
                count_occurances = count_occurances + 1
                viable_options.append(a_str)
    
    if count_occurances == 0: return None, None
    elif count_occurances == 1: 
        #print("count was 1")
        return denotation, viable_options[0]
    else:
        # First we will refrence the database to see if that can help us
        # We are assuiming there is a database to work with
        temp_hp = 0
        hp_occurance = 0
        avrg_hp = 0
        temp_cc = 0
        cc_occurance = 0
        avrg_cc = 0

        for item in database:
            if "model" in a_dict: # If a_dict has an item with a brand
                if item.get_model() == a_dict["model"]: # If the brand of item matches a brand of an item from a_dict
                    if item.get_hp_rating() != "unknown":
                        temp_hp = temp_hp + int(item.get_hp_rating())
                        hp_occurance = hp_occurance + 1

                    if item.get_cc_rating() != "unknown":  
                        temp_cc = temp_cc + int(item.get_cc_rating())
                        cc_occurance = cc_occurance + 1
            else: 
                temp_cc = 0
                temp_hp = 0
        #print(hp_occurance, temp_hp)
        if temp_hp == 0: temp_hp = None    
        else: avrg_hp = temp_hp/hp_occurance
        if temp_cc == 0: avrg_cc = None
        else: avrg_cc = temp_cc/cc_occurance

        #print(avrg_cc, avrg_hp)


        for option in viable_options:
            # Sets the best_match to the number that is closest to the average
            
            if (denotation == "cc_rating" and cc_occurance != 0):
                if avrg_cc != None:
                    #print("cc wasnt None")
                    if abs(avrg_cc - int(option)) < abs(avrg_cc - int(best_match)): 
                        best_match = option 
                        #print("cc best match is set", best_match)
            
            if (denotation == "hp_rating" and hp_occurance != 0):
                if avrg_hp != None:
                    if abs(avrg_hp - int(option)) < abs(avrg_hp - int(best_match)): 
                        best_match = option 
                        #print("hp best match is set", best_match)
                
            # Finds the number of times that the possible EP (option) has occured in the avaliable data (database)
            option_occ_dict = {}
            for option in viable_options:
                    option_occurances = 0
                    for item in database:
                        if option == item.get_cc_rating() or option == item.get_hp_rating(): # If the option can be matched
                            option_occurances = option_occurances + 1 # Add 1 to the occurence accumulator
                    option_occ_dict[option] = option_occurances # Add the times occured to the dictionary
                  
            temp_best_match = 0
            for key in option_occ_dict:
                if int(option_occ_dict[key]) > int(temp_best_match): temp_best_match = option_occ_dict[key]
                
            if best_match == temp_best_match: return denotation, best_match
                
            else:
                if any in option_occ_dict != 0: 
                    best_match = list(option_occ_dict.keys())[list(option_occ_dict.values()).index(temp_best_match)]
                    #print("best match is set in else", best_match)

        if int(best_match) == 0:
            best_match = None            
        #print("returning here", denotation, best_match)
        return denotation, best_match

def get_denotation(database, a_dict):
    # This function is responible for determining whether the power rating
    # given by the user is a hp or cc rating
    denotation = None
    empty_set = set()
    for item in database:
        try:
            if a_dict["brand"] == item.get_brand():
                item_dict = item.get_essence_as_dict()
                try: item_pv1 = item.get_cc_rating()
                except: pass
                try: item_pv2 = item.get_hp_rating()
                except: pass
                temp1 = {i for i in item_dict if item_dict[i] == item_pv1}
                temp2 = {i for i in item_dict if item_dict[i] == item_pv2}
                if temp1 != empty_set: temp = temp1
                if temp2 != empty_set: temp = temp2
                denotation = "".join(temp)
        except: pass
            # This checking the model and brand only work becasue model is overwriting
            # brand when it runs, which, is what we need. Model should be given priority
            # but there should be a descision tree to make this correct regardless of which
            # runs first
        try:
            if a_dict["model"] == item.get_model():
                item_dict = item.get_essence_as_dict()
                try: item_pv1 = item.get_cc_rating()
                except: pass
                try: item_pv2 = item.get_hp_rating()
                except: pass
                temp1 = {i for i in item_dict if item_dict[i] == item_pv1}
                temp2 = {i for i in item_dict if item_dict[i] == item_pv2}
                if temp1 != empty_set: temp = temp1
                if temp2 != empty_set: temp = temp2
                denotation = "".join(temp)
        except: pass
    return denotation
 
def find_brand(users_list, database):
    # Searches the database to see if any of the strings from the
    # users list match a brand from an item in the database
    # If a match is found that string is returned as the brand
        # !!Note!!, if there are multiple strings that would be a match
        # only the first one will be returned
    for str in users_list:
        for item in database:
            if str in item.get_brand():
                return item.get_brand()
    # If no matches were found in the database will attempt to "guess" which
    # of the users strings is the brand, if any of them are

    # Qualities of a string representing a brand
    #   The string will contain only alphabetical chars
    #NOT ENOUGH BRAINS TO FIX THIS PROBLEM
    
        

    return

def determin_amenities (users_list):
    # This function needs continued work. I believe that the directed we need to 
    # go with regards to awd and other features for vehicles, needs to be redesigned
    # completely. so for now, this function will only search the users input for a yes
    # or no and then return that string

    for a_string in users_list:
        if a_string == "yes": return a_string
        elif a_string == "no": return a_string

    return

def find_model(users_list, database, a_dist):
    for str in users_list:
        for item in database:
            if str == item.get_model():
                return str
    return

def find_deck_size(users_list):
    deck_size_list = ["42", "44", "46", "48", "50", "52", "54", "56", "60","61", "72"]
    for item in users_list:
        for num in deck_size_list:
            if item == num: return item

def find_engine_brand(users_list):
    brand_list = ["kohler", "briggs","stratton", "kawasaki"]

    for string in users_list:
        if any(char.isdigit() for char in string) ==  False:
            for brand in brand_list:
                alt_string = ''.join([i for i in string if i.isalpha()])
                if (alt_string in brand
                    and len(alt_string) > 2): return string
                if (brand in alt_string
                    and len(alt_string) > 2): return string

# Main Function
def autofill_vehicle (users_list, database):
    a_dict = {}

# If the database is empty then autofill will not be helpful
    if database == {}: return a_dict

    
# The item class req. a brand and a price so im going to start by looking for those
    brand = find_brand (users_list, database)
    try: 
        if brand != None:
            a_dict["brand"] = brand
    except: print("Could not match brand")
    
    model = find_model (users_list, database, a_dict)
    try: 
        if model != None:
            a_dict["model"] = model
    except: print("Could not match model")

    year = find_year (users_list, database, a_dict)
    try: 
        if year != None:
            a_dict["year"] = year
    except: print("Could not match year")
    
    power_type, engine_power = find_EP (users_list, database, a_dict)
    try: 
        if power_type != None and engine_power != None:
            a_dict[power_type] = engine_power
    except: print("Could not match power rating")

    price = find_price (users_list, database, a_dict)
    try: 
        if price != None:
            a_dict["price"] = price
    except: print("Could not match price")
    
    awd = determin_amenities (users_list)
    try: 
        if awd != None:
            a_dict["awd"] = awd
    except: print("Could not match amenities")
    
    deck_size = find_deck_size(users_list)
    try:
        if deck_size != None:
            a_dict["deck_size"] = deck_size
    except: print("Could not determin deck size")

    engine_brand = find_engine_brand(users_list)
    try:
        if engine_brand != None:
            a_dict["engine_brand"] = engine_brand
    except: print("Could not determin deck size")

    
    return a_dict

