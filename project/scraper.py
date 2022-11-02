from pyrsistent import s
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from time import sleep
from datetime import date, datetime

import json
import os
import requests
import uuid

class Scraper:
    def __init__(self, url: str = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E274&insId=1&radius=10.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'):
        '''
        This class is used to scrape a website and extract text and images.
        The website chosen for the task is RightMove, therefore it will scrap property details.

        Attributes:
            driver: chrome web driver
            page (int): the number of the currently scraped page.
            property number (int): the number of the current property.
            whole_query_property_link (list): list of links to all properties.
            properties_dict_list (list): list of dictionaries that store data from all properties.
            date (str): current date
            hour (str): current time
        '''
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(url) # look for all properties for sale within a 10-mile radius from Cambridge, UK
        time.sleep(2)
        
        self.page = 0
        self.property_number = 0

        self.whole_query_property_links = []
        self.properties_dict_list = []

        self.date = str(date.today())
        self.hour = datetime.now()
        self.current_time = str(self.hour.strftime("%H:%M"))

        print('\n---Program initialised.')

    def bypass_cookies(self):
        '''A method that bypasses cookies if present.'''
        try:
            self.accept_cookies_button = self.driver.find_element(By.XPATH, value='//button[@class="optanon-allow-all accept-cookies-button"]')
            self.accept_cookies_button.click()
        except:
            pass # passes if there is no cookies button
        time.sleep(2)

    ###########################################
    ###### create list of property links ######
    ###########################################

    def get_all_property_links(self):
        '''A method that acts like a crawler'''
        self.page += 1 # needs to stay here at all times
        self.all_properties_links_list = []

        self.elems = self.driver.find_elements(By.CSS_SELECTOR, value=".propertyCard-priceLink")
        self.all_properties_links_list = [elem.get_attribute('href') for elem in self.elems]
        time.sleep(2)
        # slashes the list to exclude the featured property (repeated later in the HTML code)
        self.all_properties_links_list = self.all_properties_links_list[1:]

    def create_global_list(self):
        '''A method that creates a list of links to the properties to scrape'''
        self.whole_query_property_links.extend(self.all_properties_links_list)

    def scroll_to_bottom(self):
        '''A method that scrolls to bottom of page.'''
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def move_to_the_next_page(self):
        '''A method that clicks on the 'next page' button, if present.'''
        try:
            self.move_to_next_page = self.driver.find_element(By.CSS_SELECTOR, value=".pagination-button.pagination-direction.pagination-direction--next")
            self.move_to_next_page.click()
            time.sleep(2)
        except:
            pass # passes if there is no 'next page' button
            time.sleep(2)

    ##########################################
    ###### extract all property details ######
    ##########################################

    def generate_property_ids(self):
        '''A method to generate property ids and uuid4s'''
        self.property_number += 1
        self.property_id = 'property_' + str(self.property_number)
        self.uuid4 = str(uuid.uuid4())

    def get_first_image_link(self):
        '''A method that extracts the link to the properties first image'''
        self.property_image_link_div = self.driver.find_element(By.XPATH, value='//div[@class="_2TqQt-Hr9MN0c0wH7p7Z5p"]')
        self.property_image_link_a = self.property_image_link_div.find_element(By.XPATH, value='.//meta')
        self.property_image_link = self.property_image_link_a.get_attribute('content')

        print(self.property_image_link)

    def get_property_metrics(self):
        '''A method that extracts basic property metrics (price, address)'''
        self.property_price = self.driver.find_element(By.XPATH, '//div[@class="_1gfnqJ3Vtd1z40MlC0MzXu"]').text # finds property price
        self.property_address = self.driver.find_element(By.XPATH, value='//div[@class="h3U6cGyEUf76tvCpYisik"]').text # finds property address

    def get_property_type(self):
        '''A method that extracts the property type'''
        self.property_type_div = self.driver.find_element(By.XPATH, value='//div[@class="_3OGW_s5TH6aUqi4uHum5Gy"]') # finds property type
        self.property_type = self.property_type_div.find_element(By.XPATH, value='.//p').text
            
        # fixes problems caused by type unaccuracies in the website
        if self.property_type == '3,234,766 sq. ft.':
            self.property_type = 'Land'
        elif self.property_type == 'Ask agent':
            self.property_type = 'Undefined'

    def get_property_description(self):
        '''A method that extracts the property description'''
        try: # clicks on 'read more' button in description
            self.move_to_next_page = self.driver.find_element(By.CSS_SELECTOR, value="button._33m7y0JkS3Q_2tRLrMPB9U")
            self.move_to_next_page.click()
        except:
            pass # passes if there is no read more button

        self.property_description = self.driver.find_element(By.XPATH, value='//div[@class="OD0O7FWw1TjbTD4sdRi1_"]').text # finds & stores property description

    ###################################################
    ###### stores data into list of dictionaries ######
    ###################################################

    def extract_the_data_into_a_dictionary(self):
        '''A method that creates dictionaries based on property features,
        and appends them to properties_dict_list.'''

        for property_link in self.whole_query_property_links:
            self.driver.get(property_link)
            time.sleep(2)
            
            self.properties_dictionary = {}

            self.generate_property_ids()
            self.properties_dictionary['ID'] = self.property_id
            self.properties_dictionary['UUID'] = self.uuid4

            self.get_first_image_link()
            self.properties_dictionary['Image'] = self.property_image_link
            
            self.get_property_metrics()
            self.properties_dictionary['Price'] = self.property_price
            self.properties_dictionary['Address'] = self.property_address

            self.get_property_type()
            self.properties_dictionary['Type'] = self.property_type
            
            self.get_property_description()
            self.properties_dictionary['Description'] = self.property_description

            self.properties_dictionary['Date scraped'] = self.date
            self.properties_dictionary['Time scraped'] = self.current_time

            self.properties_dict_list.append(self.properties_dictionary)
            time.sleep(2)

        print(self.properties_dict_list)

    #######################################################
    ###### download images, store data in .json file ######
    #######################################################
    
    def download_images(self):
        '''A method that utilises the links stored under the 'Image' key of properties_dict_list
        and downloads the corresponding images into local directory'''
        self.destination_folder = 'raw_data/right_move_scraper/scraped_images'

        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

        for index, self.dict in enumerate(self.properties_dict_list):
            index += 1
            
            self.image_name = f'{self.date}_{self.current_time}_image_{str(index)}.jpeg'
            self.image_path = os.path.join(self.destination_folder, self.image_name)
            self.image_url = self.dict['Image']

            img_data = requests.get(self.image_url)
            with open(self.image_path, 'wb') as handler:       
                handler.write(img_data.content)
    
    def save_data_to_json(self):
        '''A method that converts properties_dict_list into a .json file and stores it into dedicated directories'''
        self.destination_folder = 'raw_data/right_move_scraper/data'

        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

        self.file_name = 'data.json'
        self.folder_path = os.path.join(self.destination_folder, self.file_name)
        
        with open(self.folder_path, 'w', encoding='utf-8') as output:
            json.dump(self.properties_dict_list, output, ensure_ascii=False, indent=4)