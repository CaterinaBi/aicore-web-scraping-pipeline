from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Scraper:
    def __init__(self, url: str = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E274&insId=1&radius=10.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url) # look for all properties for sale within a 10-mila radius from Cambridge, UK
        self.time.sleep(2)

    # no need to bypass cookies in this website

    # creates a crawler
    def get_all_properties_in_the_page(self):
        self.property_container = self.driver.find_element(By.XPATH, value='//div[@id="l-searchResults"]')

    def extract_the_data_into_a_dictionary(self):
        pass

    def move_to_the_next_page(self):
        pass