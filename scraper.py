from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import time
from time import sleep

class Scraper:
    def __init__(self, url: str = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E274&insId=1&radius=10.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'):
        print('\nHi! I\'m Bot. I\'m now going to open the website that you chose.')
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url) # look for all properties for sale within a 10-mile radius from Cambridge, UK
        time.sleep(2)
        
        self.page = 0
        # creates list of properties from all pages
        self.whole_query_property_list = []
        # creates list of links for all properties from all pages
        self.whole_query_property_links = []

        print('We\'re in! I\'m now going to accept all cookies.')
        time.sleep(2)

    # bypasses cookies
    def bypass_cookies(self):
        try:
            # gets the accept all cookies button and clicks it
            self.accept_cookies_button = self.driver.find_element(By.XPATH, value='//button[@class="optanon-allow-all accept-cookies-button"]')
            self.accept_cookies_button.click()
            print('\nAll cookies accepted!')
        except:
            pass # passes if there is no cookies button
            print('\nThere were no cookies to accept.')
        print('\nI\'m now going to crate lists of properties and their respective links.\nThe lists will be sliced to exclude the \'featured\' property on each page.')
        time.sleep(2)

    # creates a crawler
    def get_all_properties_in_the_page(self):
        self.page =+ 1
        print(f'\nWe\'re on page {self.page}.')
        # gets the container where all properties are stored
        self.property_container = self.driver.find_element(By.XPATH, value='//*[@id="l-searchResults"]/div')
        # gets list of all properties inside the container using <div> tags that are its direct children
        # excludes list items that are ads by using @class=l-searchResult is-list, which is exclusive to properties
        self.property_list = self.property_container.find_elements(By.XPATH, value='./div[contains(@class,"l-searchResult is-list")]')
        print(f'\nNumber of properties on page {self.page} before slicing: {len(self.property_list)}\n')
        print(f'Number of properties on this page: {len(self.property_list)}\n')

        # slashes the list to exclude the first property (featured property, repeated later in the HTML code)
        self.property_list = self.property_list[1:]
        print(f'\nThe list of properties on page {self.page} is as follows:\n')
        print(f'{self.property_list}\n')

    # continues crawler   
    def get_all_property_links(self):
         # creates empty list of links to all properties
        self.all_properties_links_list = []
        # creates list of links to all properties
        self.elems = self.driver.find_elements(By.CSS_SELECTOR, value=".propertyCard-priceLink")
        self.all_properties_links_list = [elem.get_attribute('href') for elem in self.elems]
        time.sleep(2)
        print(f'We found {len(self.all_properties_links_list)} links to properties in page {self.page} before slicing.\n')
        print(f'After slicing, there are {len(self.all_properties_links_list)} links to properties in this page:')

        # slashes the list to exclude the first property (featured property, repeated later in the HTML code)
        self.all_properties_links_list = self.all_properties_links_list[1:]
        print(f'\nThe list of properties on page {self.page} is as follows:\n')
        print(f'{self.all_properties_links_list}\n')

    def create_global_list(self):
        # adds properties from current page to the global list
        self.whole_query_property_list.extend(self.property_list)
        print(f'\nThe global list of properties now includes {len(self.whole_query_property_list)} properties.')
        # adds property links from current page to the list
        self.whole_query_property_links.extend(self.all_properties_links_list)
        print(f'The global list of property links now includes {len(self.whole_query_property_links)} links.')

    def scroll_to_bottom(self):
        print('\nScrolling to the bottom of the page right now, then clicking on \'next page\'.')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # clicks on the 'next page' button
    def move_to_the_next_page(self):
        try:
            # gets the next page button and clicks it
            self.move_to_next_page = self.driver.find_element(By.CSS_SELECTOR, value=".pagination-button.pagination-direction.pagination-direction--next")
            self.move_to_next_page.click()
            time.sleep(2)
        except:
            pass # passes if there is no next page button
            print(f'\nThere\'s no \'next page\' button, looks like we reached an impasse! I think we\'re done.')

    def extract_the_data_into_a_dictionary(self):
        pass