from selenium.webdriver.chrome.options import Options
import unittest

from project.scraper import Scraper

class ScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.scraper = Scraper()

    #def test_bypass_cookies(self):
        #'''A method that tests that the accept cookies button is correctly hit when present'''
        #actual = self.scraper.bypass_cookies()

        #try:
            #expected1 = '---Cookies accepted'
            #self.assertEqual(actual, expected1)
            #print('---Accept cookies button correctly used')
        #except:
            #expected2 = '---No cookies to accept'
            #self.assertEqual(actual, expected2)
            #print('---No accept cookies button found')

    #def test_get_all_property_links(self):
        #'''A method that tests that what what is created is indeed a list, and that the original list of
        #properties is correctly sliced to exclude the first property on each page'''
        #self.scraper.bypass_cookies()
        #property_list = self.scraper.get_all_property_links()
        #list_length = 24
        #property_list_type = type(property_list)

        #self.assertIs(property_list_type, list) # checks that method returns a list
        #self.assertEqual(len(property_list), list_length) # checks that the list length is as expected

    #def test_create_global_list(self):
        #'''A method that checks that the list of property created in each loop of the program logic
        #is correctly appended to the global list'''
        #self.scraper.bypass_cookies()
        #property_list = self.scraper.get_all_property_links()
        #global_list = self.scraper.create_global_list()
        #list_length = 24
        #global_list_type = type(global_list)

        #self.assertIs(global_list_type, list) # checks that method returns a list
        #self.assertEqual(len(global_list), list_length) # checks that the list length is as expected
        #self.assertEqual(global_list, property_list) # checks that property_list is correctly appended

    #def test_scroll_to_bottom(self):
        #'''A method that tests that the document height page does not change after the first scroll i.e. is already fully loaded.'''
        #self.scraper.bypass_cookies()
        #self.scraper.scroll_to_bottom()
        #height_1 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        #self.scraper.scroll_to_bottom()
        #height_2 = self.scraper.driver.execute_script('return document.body.scrollHeight')
        #self.assertAlmostEqual(height_1/1000, height_2/1000)

    def tearDown(self):
        self.scraper.driver.quit()
        del self.scraper