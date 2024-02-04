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
        options = webdriver.FirefoxOptions()
        # options.add_argument('--headless')

        # Membuat instance WebDriver dengan opsi yang sudah dikonfigurasi
        driver = webdriver.Firefox(options=options)

        # twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')
        # print("Twitter Auth Token:", twitter_auth_token)
        #
        # driver.add_cookie({
        #     'name': 'auth_token',
        #     'value': twitter_auth_token,
        #     'domain': 'twitter.com'
        # })


        return driver
