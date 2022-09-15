from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
from time import sleep

class Scraper:
    def __init__(self, url: str = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E274&insId=1&radius=10.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url) # look for all properties for sale within a 10-mila radius from Cambridge, UK
        time.sleep(2)

    # bypasses cookies
    def bypass_cookies(self):
        try:
            # gets the accept all cookies button and clicks it
            self.accept_cookies_button = self.driver.find_element(By.XPATH, value='//button[@class="optanon-allow-all accept-cookies-button"]')
            self.accept_cookies_button.click()
        except:
            pass # passes if there is no cookies button

    # creates a crawler
    def get_all_properties_in_the_page(self):
        # gets the container where all properties are stored
        self.property_container = self.driver.find_element(By.XPATH, value='//*div[@id="l-searchResults"]')
        # gets list of all properties inside the container using <div> tags that are its direct children
        self.property_list = self.property_container.find_elements(By.XPATH, value='./div')
        # creates empty list of links to all properties
        self.all_properties_links_list = []

        # populates list
        for property in self.property_list:
            self.a_tag = property.find_element(By.TAG_NAME, value='a')
            self.link = self.a_tag.get_attribute('href')
            self.all_properties_links_list.append(self.link)
            time.sleep(2)

        # prints list of links
        print(f'There are {len(self.all_properties_links_list)} properties in this page.')
        print(self.all_properties_links_list)

    def extract_the_data_into_a_dictionary(self):
        pass

    def move_to_the_next_page(self):
        pass