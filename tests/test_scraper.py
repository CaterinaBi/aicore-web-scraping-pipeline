from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import unittest

from project.scraper import Scraper

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        '''Opens the website in headless mode'''
        self.options = Options()
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument("--disable-notifications")
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.scraper = Scraper(driver=webdriver.Chrome(options=self.options))

    def test_bypass_cookies(self):
        self.actual = Scraper.bypass_cookies()
        try:
            self.expected1 = '---Cookies accepted'
            self.assertEqual(self.actual, self.expected1)
            print('---Accept cookies button correctly used')
        except:
            self.expected2 = '---No cookies to accept'
            self.assertEqual(self.actual, self.expected2)
            print('---No accept cookies button found')

    def test_get_all_property_links(self):
        pass

    def test_create_global_list(self):
        pass

    def test_scroll_to_bottom(self):
        '''Tests that the document height page does not change after the first scroll i.e. is already fully loaded.'''
        self.scraper.driver.get('https://www.rightmove.co.uk/property-for-sale/Newmarket.html') # tests the scraper on properties for sale in Newmarket
        self.scraper.bypass_cookies()
        self.scraper.scroll_to_bottom()
        height_1 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        self.scraper.scroll_to_bottom()
        height_2 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        self.assertAlmostEqual(height_1/1000, height_2/1000, self.place==1)

    def test_move_to_the_next_page(self):
        pass

    def test_generate_property_ids(self):
        pass

    def test_get_first_image_link(self):
        pass

    def test_get_property_metrics(self):
        pass

    def test_get_property_type(self):
        pass

    def test_get_property_description(self):
        pass

    def test_extract_the_data_into_a_dictionary(self):
        pass

    def test_download_images(self):
        pass

    def test_save_data_to_json(self):
        pass