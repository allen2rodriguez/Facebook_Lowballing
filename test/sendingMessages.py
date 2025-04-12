# Description: File that sends the authors bot's messages to them
# Author: Allen Rodriguez
# Version: 1.0.0

from selenium import webdriver # To load the page and the data on it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def send_message(page, text):
    # Set up the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Open up the page
    driver.get(page)

    # Log in 
    # Press button 
    # Click email
    # Input Username and password

    #Press the ask button 
    # Put it into the text area 

    time.sleep(100)

    driver.quit()
