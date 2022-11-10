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

        #self.assertIs(type(property_list), list) # checks that method returns a list
        #self.assertEqual(len(property_list), list_length) # checks that the list length is as expected

    #def test_create_global_list(self):
        #'''A method that checks that the list of property created in each loop of the program logic
        #is correctly appended to the global list'''
        #self.scraper.bypass_cookies()
        #property_list = self.scraper.get_all_property_links()
        #global_list = self.scraper.create_global_list()
        #list_length = 24

        #self.assertIs(type(global_list), list) # checks that method returns a list
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

    #def test_move_to_the_next_page(self):
        #'''A method that tests that the next page button is correctly hit when present'''
        #actual = self.scraper.move_to_the_next_page()

        #try:
            #expected1 = '---Moved to next page'
            #self.assertEqual(actual, expected1)
            #print('---Accept cookies button correctly used')
        #except:
            #expected2 = '---No cookies to accept'
            #self.assertEqual(actual, expected2)
            #print('---No next page')

    #def test_generate_property_ids(self):
        #'''A method that tests that property ids are correctly generated'''
        #actual = self.scraper.generate_property_ids()
        #return_tuple = ('property_1', '')

        #self.assertEqual(type(return_tuple), type(actual)) # checks that method returns a tuple
        #self.assertEqual(return_tuple[0], actual[0]) # checks that the first element of the tuple is correctly generated
        #self.assertEqual(type(actual[1]), type(return_tuple[1])) # checks that the generated uuid is a string

    #def test_get_first_image_link(self):
        #self.scraper.bypass_cookies()
        #links = self.scraper.get_all_property_links()
        #link_to_test = links[0] # only tests code on first property

        #self.scraper.driver.get(link_to_test)
        #image_link = self.scraper.get_first_image_link()
        #expected_link = 'https://media.rightmove.co.uk/106k/105848/128269403/105848_100539081819_IMG_00_0000.jpeg'

        #self.assertEqual(expected_link, image_link) # checks that the link to the first property is correctly extracted

    #def test_get_property_metrics(self):
        #'''A method that tests that property address and price are correctly extracted'''
        #self.scraper.bypass_cookies()
        #links = self.scraper.get_all_property_links()
        #link_to_test = links[0] # only tests code on first property

        #self.scraper.driver.get(link_to_test)
        #actual = self.scraper.get_property_metrics()
        #return_tuple = ('£6,500,000', 'Chrishall Grange Farm, Heydon, Royston')

        #self.assertEqual(type(return_tuple), type(actual)) # checks that method returns a tuple
        #self.assertEqual(return_tuple[0], actual[0]) # checks that the first element of the tuple is correctly generated
        #self.assertEqual(return_tuple[1], actual[1]) # checks that the second element of the tuple is correctly generated

    #def test_get_property_type(self):
        #'''A method that checks that the property type is correctly extracted'''
        #self.scraper.bypass_cookies()
        #links = self.scraper.get_all_property_links()
        #link_to_test = links[0] # only tests code on first property

        #self.scraper.driver.get(link_to_test)
        #actual = self.scraper.get_property_type()
        #expected = 'Farm Land'

        #self.assertEqual(expected, actual) # checks that the property type is correctly extracted

    #def test_get_property_description(self):
        #'''A method that checks that the description is a string'''
        #self.scraper.bypass_cookies()
        #links = self.scraper.get_all_property_links()
        #link_to_test = links[0] # only tests code on first property

        #self.scraper.driver.get(link_to_test)
        #description = self.scraper.get_property_description()
        #expected_type = str
        #description_length = 12548

        #self.assertEqual(type(description), expected_type) # checks that the description is a string
        #self.assertEqual(len(description), description_length) # checks that the description length is as expected

    #def test_extract_the_data_into_a_dictionary(self):
        #'''A method that checks that the dictionary is correctly created'''
        #self.scraper.bypass_cookies()
        #links = self.scraper.get_all_property_links()
        #link_to_test = links[0] # only tests code on first property

        #self.scraper.driver.get(link_to_test)
        #dictionary_list = self.scraper.extract_the_data_into_a_dictionary()

        #for dictionary in dictionary_list:
            #assert dictionary[0] == "ID"
            #assert dictionary[1] == "UUID"
            #assert dictionary[2] == "Image"
            #assert dictionary[3] == "Price"
            #assert dictionary[4] == "Address"
            #assert dictionary[5] == "Type"
            #assert dictionary[6] == "Description"

    

    def tearDown(self):
        self.scraper.driver.quit()
        del self.scraper