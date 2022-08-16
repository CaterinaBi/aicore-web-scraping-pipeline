from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class Scraper:
    def __init__(self, url: str = 'https://www.cnc.fr/professionnels/jeunes-professionnels/scenariotheque/fiction?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_Z4ziKksles4L&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_Z4ziKksles4L_delta=60&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_Z4ziKksles4L_cur=1'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(url)
        self.button_id = str

    def click_button(self):
        click_button = self.driver.find_element(By.XPATH, self.button_id)
        click_button = self.click()

    def bypass_cookies(self):
        bypass_cookies = self.click_button(button_id= '//button[@id="tarteaucitronManager"]')

    def download_files(self):
        pass

    def move_to_following_page(self):
        pass