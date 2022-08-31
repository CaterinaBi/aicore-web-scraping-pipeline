from scraper import Scraper
import time 

def run_scraper():
    bot = Scraper()
    time.sleep(5)
    bot.bypass_cookies()
    time.sleep(5)
    bot.scroll_page()

if __name__ == '__main__':
    # bot = Scraper()
    # bot_2 = Scraper('https://lecteursanonymes.org/scenario/')
    # bot_3 = Scraper('https://www.simplyscripts.com/non_english_scripts.html')
    # bot_4 = Scraper('https://www.ebooksgratuits.com/ebooks.php')
    run_scraper()

