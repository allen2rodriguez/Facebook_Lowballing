# Description: This page will be used to scrape the data off a listing on Facebook Marketplace or Offerup 
# Author: Allen Rodriguez 
# Version: 1.0.0

from selenium import webdriver # To laod the page and the data on it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup # Parse the data 
import time
# Consider importing json to turn the data into JSON

def web_scrape(page):
    # Set up the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)


    # Open up the page
    driver.get(page)

    time.sleep(100)
    
    
    # Log into Facebook
    # Username: class="inputtext _55r1 inputtext _1kbt inputtext _1kbt"
    # Password: class="inputtext _55r1 inputtext _9npi inputtext _9npi"
    

    # Parse the HTML    
    #soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #title = soup.find('h1') 
    # TODO: add in price, description, sellers_name and if applicable "About this vehicle" information

    driver.quit()
    
def main():
    page = input("Enter the link: ")
    web_scrape(page)
    title = web_scrape(page)

    # print(title.text)

if __name__ == '__main__':
    # This will allow the module to be run directly or imported without executing the code block below it
    main()
    print("Web scraping completed.")