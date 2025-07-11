from selenium import webdriver # To load the page and the data on it
from selenium.webdriver.common.by import By

class offerUpBot:
    def __init__(self, page: str):
        """
        Initializes the OfferUp bot with the specified AI model type and page. That it can always pull from
        """
        self.page = page
        # Set up the Webdriver
        service = webdriver.chrome.service.Service(executable_path="chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new') # Don't want to see the browser pop up unless debugging
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)  # Wait for elements to load
        # Add in cookies (potentially here!)

    def web_scrape(self) -> list:
        """
        Begins the process of scraping the OfferUp listing page for relevant information that can be passed on to the LLM.
        Parameters
        ----------
        page : str
            The URL of the OfferUp listing page to scrape.
        Returns
        -------      
        list
            A list :
                [0] title
                [1] price
                [2] description
                [3] seller's name
        """
        self.driver.get(self.page)
        # Gather Info: Title, Description, Price, Seller's Name
        title = self.driver.find_element(By.TAG_NAME, "h1").text
        price = self.driver.find_element(By.TAG_NAME,'p').text
        # posted_date
        category = self.driver.find_element(By.XPATH, "//p[span[contains(text(), 'Listed in categories:')]]").text
        description = self.driver.find_element(By.XPATH, "//div[@data-testid='itemDescription']/following::p[1]").text
        sellers_name = self.driver.find_element(By.XPATH, "//h2[text()='Sold by']/following::p[1]").text
        # Always quit the driver at the end of the scrape to free up resources
        self.driver.quit()
        return [
            title, 
            price, 
            category,
            description if description else "No description given",
            sellers_name if sellers_name else "No seller name"
            ]

    # TBD - Finish this method after getting the extension working (AKA this is the last thing to do)
    def send_message(self, model: str, message: str, username: str, password: str) -> None:
        pass
        """
        print("\nSending message to the author of the post...")
        driver.get(page)
        # Log in
        driver.find_elements(By.TAG_NAME, "button")[9].click()
        driver.find_elements(By.TAG_NAME, "button")[-1].click() # Press the continue with Email
        driver.find_elements(By.TAG_NAME, "button")[-1].click()
        # Continue working on after finishing with above 
        # Input Username and password
        email_input = driver.find_element(By.NAME, "email")
        email_input.clear()
        email_input.send_keys(username)
        password_input = driver.find_element(By.NAME, "password")
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(30)
        driver.quit()
        """