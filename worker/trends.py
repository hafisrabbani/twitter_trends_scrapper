from selenium import webdriver
from dotenv import load_dotenv
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from utils.utility import write_to_file, remove_char,get_first_element_separator
import os

load_dotenv(".env")

TWITTER_AUTH_TOKEN = os.getenv('TWITTER_AUTH_TOKEN')
TWITTER_PATH_TRENDS = "https://twitter.com/i/trends"

options = webdriver.ChromeOptions()
# options.add_argument('--headless')

# set cookie
driver = webdriver.Chrome(options=options)
cookie_dict = {
    'name': 'auth_token',
    'value': TWITTER_AUTH_TOKEN,
    'domain': '.twitter.com',
    'path': '/',
    'secure': True,
    'httpOnly': True
}
driver.get("https://twitter.com")
driver.add_cookie(cookie_dict)
print("Cookie added....\n")
# move to trends page
driver.get(TWITTER_PATH_TRENDS)
print("Moved to trends page....\n")
# refresh page
driver.refresh()
# wait for page to load
driver.implicitly_wait(10)


# get all cookies
cookies = driver.get_cookies()
print("Cookies:", cookies)

def get_trends(driver):
    trends_list = []
    trend_data = driver.find_elements(By.CSS_SELECTOR, ".css-175oi2r.r-1adg3ll.r-1ny4l3l")
    print("Getting data started.......\n")
    for index, trend in enumerate(trend_data):
        if index == 0:
            continue
        trend_info = {}
        try:
            trend_info['category'] = get_first_element_separator(trend.text, "\n")
        except NoSuchElementException:
            trend_info['category'] = None
        try:
            trend_info['hashtags'] = trend.find_element(By.CSS_SELECTOR, ".css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e").text
            if "#" not in trend_info['hashtags']:
                trend_info['type'] = "text"
            else:
                trend_info['type'] = "hashtag"
        except NoSuchElementException:
            trend_info['hashtags'] = None
        try:
            trend_info['post_count'] = remove_char(trend.find_element(By.CSS_SELECTOR, ".css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-n6v787.r-1cwl3u0.r-16dba41.r-14gqq1x").text, "posts")
        except NoSuchElementException:
            trend_info['post_count'] = None
        trends_list.append(trend_info)
    return trends_list

result = get_trends(driver)
print("Result:", result)
write_to_file(result)
driver.close()