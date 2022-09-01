from scraper import Scraper

if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()
    bot.get_all_properties_in_the_page()