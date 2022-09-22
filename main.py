from scraper import Scraper
import time

if __name__ == '__main__':
    bot = Scraper()
    bot.bypass_cookies()
    bot.get_all_properties_in_the_page()
    bot.scroll_to_bottom()
    time.sleep(5)
    bot.driver.quit()