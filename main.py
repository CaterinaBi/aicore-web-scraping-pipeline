from scraper import Scraper

if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()
    while True:
        bot.get_all_properties_in_the_page()
        bot.create_global_list()
        bot.scroll_to_bottom()
        bot.move_to_the_next_page()
    # bot.driver.quit()