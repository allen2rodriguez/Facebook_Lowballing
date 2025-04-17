# Description: File that sends the authors bot's messages to them
# Author: Allen Rodriguez
# Version: 1.0.0

from selenium import webdriver # To load the page and the data on it
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def send_message(page: str, text: str, username: str, password: str):
    # Set up the WebDriver
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Open up the page
    driver.get(page)

    # Log in
    button = driver.find_elements(By.TAG_NAME, "button")
    login_button = button[9]
    login_button.click()

    # Continue with Email
    button1 = driver.find_elements(By.TAG_NAME, "button")
    email_button = button1[-1] # After updating the button list, this new button should be the last
    email_button.click()

    # Log in 
    button2 = driver.find_elements(By.TAG_NAME, "button")
    login_button = button2[-1] # After updating the button list, this new button should be the last 
    login_button.click()

    # Input Username and password
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys(username)

    password_input = driver.find_element(By.NAME, "password")
    password_input.clear()
    password_input.send_keys(password)

    # Click the login button
    button3 = driver.find_elements(By.TAG_NAME, "button")
    login_button = button3[-2] # After updating the button list, this new button should be the last
    login_button.click()

    # Complete Recaptcha
    time.sleep(30) # Allow enough time for user to do the captcha

    #Press the ask button 
    # Put it into the text area 

    time.sleep(100)

    driver.quit()
