# Brian Hayes
# 27 Apr 2023

from selenium import webdriver
import urllib.request


def get_img_from_web(list_of_img_srcs):
    global driver
    driver = webdriver.Chrome()
    driver.minimize_window()
    list_of_img_locals = dwnld_imgs (list_of_img_srcs)
    
    driver.quit()
    return list_of_img_locals

def dwnld_imgs (list_of_img_srcs):
    list_of_img_locals = []
    name = 0
    for tup in list_of_img_srcs:
        urllib.request.urlretrieve(tup[1], "C:/Users/hayesb3/Geany 1.38/Program Files/marketplace/the-grey-market/search resules/"+str(name)+".jpg")
        img_path = "C:/Users/hayesb3/Geany 1.38/Program Files/marketplace/the-grey-market/search resules/"+str(name)+".jpg"
        list_of_img_locals.append(img_path)	
        name += 1
    return list_of_img_locals





if __name__ == "__main__": 
    src = "https://scontent-ord5-1.xx.fbcdn.net/v/t45.5328-4/343342645_6144760072305527_7452286811827479001_n.jpg?stp=c43.0.260.260a_dst-jpg_p261x260&_nc_cat=109&ccb=1-7&_nc_sid=c48759&_nc_ohc=jGUTBqFtK8wAX9iHqAa&_nc_ht=scontent-ord5-1.xx&oh=00_AfBAy1cl0zQkYMPtsOqvDtQbInCDr3DJjZkn_EGl8-SDMA&oe=64504061"
    get_img_from_web(src, "test")


