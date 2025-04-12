# Description: This page is used to scrape data off of Offerup listings to be pased on to my LMM
# Author: Allen Rodriguez
# Version: 1.0.0

from selenium import webdriver # To load the page and the data on it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#import time

def web_scrape(page):
    # Set up the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Open up the page
    driver.get(page)

    # Gather Info: Title, Description, Price, Seller's Name
    title = driver.find_element(By.TAG_NAME, "h1")

    info = driver.find_elements(By.TAG_NAME,'p') # info[0] is the price, info[x] is the description,

    price = info[0].text

    description = [
        element for element in info 
        if "MuiTypography-root MuiTypography-body1 MuiTypography-colorTextPrimary" 
        in element.get_attribute("class")
        ]
    description_text = [element.text for element in description]    

    sellers_name = [
        element for element in info 
        if "MuiTypography-root MuiTypography-subtitle1 MuiTypography-colorTextPrimary" 
        in element.get_attribute("class")]
    sellers_text = sellers_name[0].text if sellers_name else "No seller name found"

    listing = [title.text, price, description_text[-1], sellers_text]

    driver.quit()

    return listing  