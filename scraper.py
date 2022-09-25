from pyrsistent import s
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
        print('\nWe\'re in! I\'m now going to accept all cookies.')
        
        self.page = 0
        # creates list of properties from all pages
        self.whole_query_property_list = []
        # creates list of links for all properties from all pages
        self.whole_query_property_links = []

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

    # creates a crawler # think of a way to get rid of this part of the crawler
    # def get_all_properties_in_the_page(self):
        # gets the container where all properties are stored
        # self.property_container = self.driver.find_element(By.XPATH, value='//*[@id="l-searchResults"]/div')
        # gets list of all properties inside the container using <div> tags that are its direct children
        # excludes list items that are ads by using @class=l-searchResult is-list, which is exclusive to properties
        # self.property_list = self.property_container.find_elements(By.XPATH, value='./div[contains(@class,"l-searchResult is-list")]')
        # print(f'\nNumber of properties on page {self.page} before slicing: {len(self.property_list)}\n')
        # print(f'Number of properties on this page: {len(self.property_list)}\n')

        # slashes the list to exclude the first property (featured property, repeated later in the HTML code)
        # self.property_list = self.property_list[1:]
        # print(f'\nThe list of properties on page {self.page} is as follows:\n')
        # print(f'{self.property_list}\n')

    # creates crawler   
    def get_all_property_links(self):
        self.page =+ 1
        print(f'\nWe\'re on page {self.page} now.')
        # creates empty list of links to all properties
        self.all_properties_links_list = []
        # creates list of links to all properties
        self.elems = self.driver.find_elements(By.CSS_SELECTOR, value=".propertyCard-priceLink")
        self.all_properties_links_list = [elem.get_attribute('href') for elem in self.elems]
        time.sleep(2)
        print(f'We found {len(self.all_properties_links_list)} links to properties in page {self.page} before slicing.\n')
         # slashes the list to exclude the first property (featured property, repeated later in the HTML code)
        self.all_properties_links_list = self.all_properties_links_list[1:]
        print(f'After slicing, there are {len(self.all_properties_links_list)} links to properties in this page:')
        # print(f'\nThe list of properties on page {self.page} is as follows:\n')
        # print(f'{self.all_properties_links_list}\n')

    def create_global_list(self):
        # adds properties from current page to the global list
        # self.whole_query_property_list.extend(self.property_list)
        # print(f'\nThe global list of properties now includes {len(self.whole_query_property_list)} properties.')
        # adds property links from current page to the list
        self.whole_query_property_links.extend(self.all_properties_links_list)
        print(f'The global list of property links now includes {len(self.whole_query_property_links)} links.')

    def scroll_to_bottom(self):
        print('\nScrolling to the bottom of the page right now, then clicking on \'next page\'.')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    # clicks on the 'next page' button
    def move_to_the_next_page(self):
        self.link_collection_terminated = bool
        try:
            # gets the next page button and clicks it
            self.move_to_next_page = self.driver.find_element(By.CSS_SELECTOR, value=".pagination-button.pagination-direction.pagination-direction--next")
            self.move_to_next_page.click()
            time.sleep(2)
            self.link_collection_terminated = False
        except:
            pass # passes if there is no next page button
            self.link_collection_terminated = True
            print(f'\nThere\'s no \'next page\' button, looks like we reached an impasse! I think we\'re done.')
            time.sleep(2)
            print(f'\nThe list of property links that I have extracted is as follows:\n')
            print(f'{self.whole_query_property_links}\n')
            time.sleep(2)

    def extract_first_property_image(self):
        pass

    def extract_textual_data(self):
        pass

    # def extract_the_data_into_a_dictionary(self):
        # print('Hold on, I\'m going to extract all property details now. This might take a while...')
        # self.data_collection_terminated = bool
        # self.properties_dictionnary = {'ID': [], 'Image': [], 'Price': [], 'Address': [], 'Bedrooms': [], 'Bathrooms': [], 'Description': []}
        # Iterate through the list of links, and for each iteration, visit the corresponding URL
        # Sleep
        # Extract the information of the property
        # Visit the next URL

        # for link in self.whole_query_property_links:
            # self.property_id = 
            # self.property_image_link = 
            # self.property_price = self.driver.find_element(by=By.XPATH, value='//p[@data-testid="price"]').text
            # self.properties_dictionnary['Price'].append(self.price)
            # self.property_address = self.driver.find_element(by=By.XPATH, value='//address[@data-testid="address-label"]').text
            # self.properties_dictionnary['Address'].append(self.address)
            # self.property_bedrooms = self.driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
            # self.properties_dictionnary['Bedrooms'].append(self.bedrooms)
            # self.property_bathrooms = self.driver.find_element(by=By.XPATH, value='//div[@class="c-PJLV c-PJLV-iiNveLf-css"]').text
            # self.properties_dictionnary['Bathrooms'].append(self.bathrooms)
            # self.div_tag = self.driver.find_element(by=By.XPATH, value='//div[@data-testid="truncated_text_container"]')
            # self.span_tag = self.div_tag.find_element(by=By.XPATH, value='.//span')
            # self.description = self.span_tag.text
            # self.properties_dictionnary['Description'] = self.description

            # sets the task as completed
            # self.data_collection_terminated = True