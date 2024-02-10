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
        options.add_argument("--window-size=1920,1080")
        user_agent = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)

        return driver
