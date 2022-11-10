from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import unittest

from project.scraper import Scraper

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    def test_bypass_cookies(self):
        '''A method that tests that the accept cookies button is correctly hit when present'''
        actual = self.scraper.bypass_cookies()

        try:
            expected1 = '---Cookies accepted'
            self.assertEqual(actual, expected1)
            print('---Accept cookies button correctly used')
        except:
            expected2 = '---No cookies to accept'
            self.assertEqual(actual, expected2)
            print('---No accept cookies button found')

    def test_get_all_property_links(self):
        '''A method that tests that what what is created is indeed a list, and that the original list of
        properties is correctly sliced to exclude the first property on each page'''
        self.scraper.bypass_cookies()
        property_list = self.scraper.get_all_property_links()
        list_length = 24
        property_list_type = type(property_list)

        self.assertIs(property_list_type, list) # checks that method returns a list
        self.assertEqual(len(property_list), list_length) # checks that the list length is as expected

    # def test_create_global_list(self):
        # pass

    # def test_scroll_to_bottom(self):
        # '''Tests that the document height page does not change after the first scroll i.e. is already fully loaded.'''
        # self.scraper.driver.get('https://www.rightmove.co.uk/property-for-sale/Newmarket.html') # tests the scraper on properties for sale in Newmarket
        # self.scraper.bypass_cookies()
        # self.scraper.scroll_to_bottom()
        # height_1 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        # self.scraper.scroll_to_bottom()
        # height_2 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        # self.assertAlmostEqual(height_1/1000, height_2/1000, self.place==1)

    # def test_move_to_the_next_page(self):
        # pass

    # def test_generate_property_ids(self):
        # pass

    # def test_get_first_image_link(self):
        # pass

    # def test_get_property_metrics(self):
        # pass

    # def test_get_property_type(self):
        # pass

    # def test_get_property_description(self):
        # pass

    # def test_extract_the_data_into_a_dictionary(self):
        # pass

    # def test_download_images(self):
        # pass

    # def test_save_data_to_json(self):
        # pass

    def tearDown(self):
        self.scraper.driver.quit()
        del self.scraper