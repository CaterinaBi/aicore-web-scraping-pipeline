from scraper import Scraper

import json

if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()

    while bot.collection_terminated == False:
        bot.get_all_property_links()
        bot.create_global_list()
        bot.scroll_to_bottom()
        bot.move_to_the_next_page()
        break

    bot.extract_the_data_into_a_dictionary()
    print('\nHurray! The job is done :)')

    bot.save_data_to_json()