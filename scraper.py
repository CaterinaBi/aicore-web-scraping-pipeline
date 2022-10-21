from pyrsistent import s
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import time
from time import sleep

import json
import requests
import uuid

class Scraper:
    def __init__(self, url: str = 'https://www.rightmove.co.uk/property-for-sale/find.html?searchType=SALE&locationIdentifier=REGION%5E274&insId=1&radius=10.0&minPrice=&maxPrice=&minBedrooms=&maxBedrooms=&displayPropertyType=&maxDaysSinceAdded=&_includeSSTC=on&sortByPriceDescending=&primaryDisplayPropertyType=&secondaryDisplayPropertyType=&oldDisplayPropertyType=&oldPrimaryDisplayPropertyType=&newHome=&auction=false'):
        print('\n---Program initialised.')
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(url) # look for all properties for sale within a 10-mile radius from Cambridge, UK
        time.sleep(2)
        
        self.page = 0
        self.property_number = 0

        self.whole_query_property_list = [] # properties from all pages
        self.whole_query_property_links = [] # links to all properties from all pages
        self.properties_dict_list = [] # store property dictionaries

    def __bypass_cookies(self):
        try:
            self.accept_cookies_button = self.driver.find_element(By.XPATH, value='//button[@class="optanon-allow-all accept-cookies-button"]')
            self.accept_cookies_button.click()
        except:
            pass # passes if there is no cookies button
        time.sleep(2)

    ###########################################
    ###### create list of property links ######
    ###########################################

    def __get_all_property_links(self):
        self.page += 1 # needs to stay here at all times
        self.all_properties_links_list = []

        self.elems = self.driver.find_elements(By.CSS_SELECTOR, value=".propertyCard-priceLink")
        self.all_properties_links_list = [elem.get_attribute('href') for elem in self.elems]
        time.sleep(2)
        # slashes the list to exclude the featured property (repeated later in the HTML code)
        self.all_properties_links_list = self.all_properties_links_list[1:]

    def __create_global_list(self):
        self.whole_query_property_links.extend(self.all_properties_links_list)

    def __scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def __move_to_the_next_page(self):
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

    def __generate_property_ids(self):
        self.property_number += 1
        self.property_id = 'property_' + str(self.property_number) # generates & stores property IDs
        self.uuid4 = str(uuid.uuid4()) # generates & stores property UUIDs

    def __get_floorplan_image_link(self):
        self.property_image_link_div = self.driver.find_element(By.XPATH, value='//div[@class="mtyLjuu2GD7KK4pvhCkS5"]') # extracts & stores property floorplan image link
        self.property_image_link_div_a = self.property_image_link_div.find_element(By.TAG_NAME, 'a')
        self.property_image_link = self.property_image_link_div_a.get_attribute('href')

    def __get_property_metrics(self):
        self.property_price = self.driver.find_element(By.XPATH, '//div[@class="_1gfnqJ3Vtd1z40MlC0MzXu"]').text # finds & stores property price
        self.property_address = self.driver.find_element(By.XPATH, value='//div[@class="h3U6cGyEUf76tvCpYisik"]').text # finds & stores property address
        self.property_type_div = self.driver.find_element(By.XPATH, value='//div[@class="_3OGW_s5TH6aUqi4uHum5Gy"]') # finds & stores property type
        self.property_type = self.property_type_div.find_element(By.XPATH, value='.//p').text
            
         # fix problems caused by type unaccuracies in the website
        if self.property_type == '3,234,766 sq. ft.':
            self.property_type = 'Land'
        elif self.property_type == 'Ask agent':
            self.property_type = 'Undefined'

        if self.property_type == 'Land' or self.property_type == 'Undefined':
            self.property_bedrooms = 'NONE'
        else: 
            self.property_bedrooms_div = self.driver.find_element(By.XPATH, value='//div[2][@class="_3gIoc-NFXILAOZEaEjJi1n"]') # finds & stores bedroom number
            self.property_bedrooms = self.property_bedrooms_div.find_element(By.XPATH, value='.//p').text

    def __get_property_description(self):
        try: # clicks on 'read more' button in description
            self.move_to_next_page = self.driver.find_element(By.CSS_SELECTOR, value="button._33m7y0JkS3Q_2tRLrMPB9U")
            self.move_to_next_page.click()
        except:
            pass # passes if there is no read more button

        self.property_description = self.driver.find_element(By.XPATH, value='//div[@class="OD0O7FWw1TjbTD4sdRi1_"]').text # finds & stores property description

    ###################################################
    ###### stores data into list of dictionaries ######
    ###################################################

    def __extract_the_data_into_a_dictionary(self):
        self.properties_dictionary = {}

        for property_link in self.whole_query_property_links:
            self.driver.get(property_link)
            time.sleep(2)

            self.generate_property_ids()
            self.properties_dictionary['ID'] = self.property_id
            self.properties_dictionary['UUID'] = self.uuid4

            self.get_floorplan_image_link()
            self.properties_dictionary['Image'] = self.property_image_link
            
            self.get_property_metrics()
            self.properties_dictionary['Price'] = self.property_price
            self.properties_dictionary['Address'] = self.property_address
            self.properties_dictionary['Type'] = self.property_type
            self.properties_dictionary['Bedrooms'] = self.property_bedrooms
            
            self.get_property_description()
            self.properties_dictionary['Description'] = self.property_description

            self.properties_dict_list.append(self.properties_dictionary) # appends dictionary to properties dictionaries list
            time.sleep(2)

            # prints created list of properties dictionaries
            print(f'\n{self.properties_dict_list}')

    #######################################################
    ###### download images, store data in .json file ######
    #######################################################

    def __download_images(self):
        self.image_id = 0
        for self.dict in self.properties_dict_list:
            self.image_id += 1
            self.image_name = 'image_' + str(self.image_id) + '.jpg'
            self.image_url = self.dict['Image']

            # downloads image as .jpg file
            img_data = requests.get(self.image_url).content
            with open(self.image_name, 'wb') as handler:       
                handler.write(img_data)
    
    def __save_data_to_json(self):
        with open("data.json", "w") as outfile:
            json.dump(self.properties_dict_list, outfile)