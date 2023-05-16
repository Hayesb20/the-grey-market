# Brian Hayes
# 24 Apr 2023

import sys
sys.path.append("marketplace")
sys.path.append("marketplace/modules")

from selenium import webdriver
from selenium.webdriver.common.keys     import Keys
from selenium.webdriver.common.by       import By
from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.support.ui      import WebDriverWait
from selenium.webdriver.chrome.options  import Options

from user import user_info
from load_and_save_files import save_file
#from database_manager import Database_Manager as DM

from datetime import datetime
import time
import random


def scrape_init():
    catagory = input(" What am I looking for? ")
    x = input(" How many listings do you want me to look for? ")
    #catagory = "zeroturn mowers"
    #x = "2"
    print(" Alright! It might take me a few minutes to get them all.")
    data = scrape_fbm(num = int(x), catagory = catagory)
    # Need to add protections. num has to be a number.
    print(" Alright, I have it!")
    options()
    answer = input(" What should I do with the results? ")
    #answer = "print"
    i = 0
    while i < 1:
        match answer:
            case "print" : save_file(database=data, filepath=get_file_name(catagory))
            #case "save results"  : save_scraped_results(data)                
            case "other" : answer = input(" I'm sorry I didn't get that ")
            case "no": 
                i+=1 
                return
        answer = input(" Okay, I printed the resulets. Is there anything else? ")
    

def get_file_name(search_term):
    name = "Search Results for " + search_term + " "
    date = datetime.strftime(datetime.now(),"%H %M %d %b %Y")
    filepath = "C:/Users/hayesb3/Geany 1.38/Program Files/marketplace/the-grey-market/search results/"
    file_name = filepath + name + date + ".docx"
    return file_name

def scrape_fbm(num, catagory):
    # Open the web browser and navigating to Facebook
    start_session()
        
    # GETTING TO THE MARKET
    login() # Log into Facebook
    time.sleep(get_rand_wait_time("long")) # Wait for Facebook homepage to load in
    go_to_marketplace() # Navigate to the marketplace page

    # SEARCHING THE MARKET
    search_item(catagory)
    time.sleep(get_rand_wait_time("medium"))        
    data = scrape_listings(num)

    # CLEAN UP
    close_session()
    
    return data
       
def scrape_listings(num):
    # num represents how many listings the user wants to scrape for
    list_of_data = []

    wait_for_element_xpath('//div[@ class="x9f619 x78zum5 x1iyjqo2 x5yr21d x4p5aij x19um543 x1j85h84 x1m6msm x1n2onr6 xh8yej3"]')
    img_list = driver.find_elements(By.XPATH, '//div[@ class="x9f619 x78zum5 x1iyjqo2 x5yr21d x4p5aij x19um543 x1j85h84 x1m6msm x1n2onr6 xh8yej3"]/img')

    #print(img_list)

    wait_for_element_xpath('//div[@ class="x3ct3a4"]')
    list = driver.find_elements(By.XPATH, '//div[@ class="x3ct3a4"]/a')



    if len(list) < num:
        while len(list) < num:
            load_more_listings()
            list = driver.find_elements(By.XPATH, '//div[@ class="x3ct3a4"]/a')
            img_list = driver.find_elements(By.XPATH, '//div[@ class="x1n2onr6"]/img')

    list = list[0:num]
    img_list = img_list[0:num]
    
    for lstrings, limgs in zip(list, img_list): 
        # Variables are init to empty strings to provide clean variables
        # for each item. Otherwise if an item is missing a description
        # the description from the previous item will be used
        pdl = ""
        usr_cmnts = ""
        img_src = limgs.get_attribute('src')

        try: pdl = lstrings.text # Gets the Price, Description, and Location of the listing
        except: pass
        
        driver.execute_script("arguments[0].click();", lstrings) # Clicks on the listing
        time.sleep(get_rand_wait_time("medium")) # Allows time for the listing to load

        try: usr_cmnts = driver.find_element(By.XPATH, '//div[@ class="xz9dl7a x4uap5 xsag5q8 xkhd6sd x126k92a"]').text # Gets the lister's comments 
        except: pass

        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform() # Returns to the privious page
        time.sleep(get_rand_wait_time("medium")) # Must have a wait time so that the next listing's information is avaliable for pdl
        
        list_of_data.append((str(pdl) + "\n" + str(usr_cmnts), img_src))

    return list_of_data

def load_more_listings():
    try:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)   
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(get_rand_wait_time("short")) # Allows time for the listings to load
    except: print("could not load more listings")

def search_item(item):
    # This function will try to find the FBM search box and type into it the "item"
    # then press the enter key to seach FBM for that item
    wait_for_element_xpath('//*[@aria-label="Search Marketplace"]') # Waits for the marketplace button to become avaliable                                  
    fbm_search_bar = driver.find_element(By.XPATH, '//*[@aria-label="Search Marketplace"]') # Finds the search bar
    fbm_search_bar.send_keys(item) # Seands the string to the search bar
    driver.find_element(By.XPATH, '//*[@aria-label="Search Marketplace"]').send_keys(Keys.RETURN) # Presses the enter key

def wait_for_element_xpath(element):
    wait = WebDriverWait(driver,30)
    wait.until(EC.element_to_be_clickable((By.XPATH, element)))

def get_rand_wait_time(duration):
    match duration:
        case "short":   return random.randint(1, 2)
        case "medium":  return random.randint(2, 4)
        case "long":    return random.randint(4, 8)

def login():
    # Find and fill in the password area
    email_area = driver.find_element("name", "email")
    email_area.send_keys(user_info["fb_email"])

    # Find and fill in the password area
    password_area = driver.find_element("name", "pass")
    password_area.send_keys(user_info["fb_pw"])

    # Find and click the login button
    login_button = driver.find_element("name", "login")
    driver.execute_script("arguments[0].click();", login_button)

def go_to_marketplace():
    wait_for_element_xpath('//*[@aria-label="Marketplace"]')
    market_button = driver.find_element("xpath", '//*[@aria-label="Marketplace"]')
    driver.execute_script("arguments[0].click();", market_button)

def start_session():
    global driver
    optObj = Options()
    optObj.headless = False # I would like to be able to scrape headlessly but idk how
    driver = webdriver.Chrome(options = optObj)
    driver.minimize_window()
    url = "https://www.facebook.com/login"
    driver.get(url)
    
def close_session():
    driver.quit ()

def options():
	options_list = ["\n Print : I,ll make a docx file and print the results there",
                    " Save results : I'll try to save all the results in my database. "
                    + "\n I will try to avoid duplicates"
                    " Nothing : I'll forget it all and we will return to the main menu"
					]
	for option in options_list: print(option)    

if __name__ == '__main__': scrape_init()