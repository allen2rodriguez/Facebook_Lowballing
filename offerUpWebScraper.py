# Description: This page is used to scrape data off of Offerup listings to be pased on to my LMM
# Author: Allen Rodriguez
# Version: 1.0.0

# Where I'm leaving off: Still trying to find a way to differentiate the description text from the other text on the page

from selenium import webdriver # To load the page and the data on it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def web_scrape(page):
    # Set up the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Open up the page
    driver.get(page)

    # Gather Info: Title, Description, Price, Seller's Name
    title = driver.find_element(By.TAG_NAME, "h1")
    info = driver.find_elements(By.TAG_NAME,'p') # info[0] is the price, info[x] is the description,
    info_text = [element.text for element in info] # Get the text from each element
    description = driver.find_elements(By.CLASS_NAME, "MuiTypography-root.MuiTypography-body1.MuiTypography-colorTextPrimary")
    description_text = [element.text for element in description]    

    listing = [title.text, info_text, description_text]

    driver.quit()

    return listing  






'''======================================================================================================'''

def main():
    page = input("Enter the Offerup listing link: ")
    listing = web_scrape(page)

    # DEBUG: Print the listing information to verify it was scraped correctly
    print(listing[0])
    print(listing[2])



if __name__ == '__main__':
    main()
    print("Web scraping completed.")