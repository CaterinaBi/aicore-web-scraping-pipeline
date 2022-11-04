from project.scraper import Scraper
import unittest

class ScraperTestCase(unittest.TestCase):
    bot = Scraper(url='https://www.rightmove.co.uk/property-for-sale/Newmarket.html') # tests the scraper on properties for sale in Newmarket

    def test_bypass_cookies(self):
        pass

    def test_get_all_property_links(self):
        pass

    def test_create_global_list(self):
        pass

    def test_scroll_to_bottom(self):
        pass

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

    