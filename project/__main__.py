from scraper import Scraper

if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()

    while bot.page <2: # use while=True when scraping all pages
        bot.get_all_property_links()
        bot.create_global_list()
        bot.scroll_to_bottom()
        bot.move_to_the_next_page()
    
    bot.extract_the_data_into_a_dictionary()
    print('\n---Dictionary correctly created.')
    bot.download_images()
    print('\n---Images correctly downloaded.')
    bot.save_data_to_json()
    print('\n---Data correctly saved locally.')