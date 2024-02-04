from config.webdriver import WebDriver
from selenium.webdriver.common.by import By

web_driver = WebDriver()
web_driver = web_driver.get_driver()

web_driver.get("https://example.com")
element = web_driver.find_element(By.TAG_NAME, "h1")
print(element.text)
