from selenium import webdriver
from dotenv import load_dotenv
import os


class WebDriver:
    def __init__(self):
        load_dotenv(".env")
        self.driver = None

    def get_driver(self):
        if not self.driver:
            self.driver = self._create_driver()
        return self.driver

    def close_driver(self):
        if self.driver:
            self.driver.close()
            self.driver.quit()
            self.driver = None

    def _create_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)

        return driver
