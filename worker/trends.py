from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from configs.webdriver import WebDriver
from utils.utility import write_to_file, remove_char, get_first_element_separator, format_number
from models.trends import TwitterTrends
import time
class TwitterTrendsScraper:
    TWITTER_PATH_TRENDS = "https://twitter.com/i/trends"
    TWITTER_PATH = "https://twitter.com"

    def __init__(self):
        print("Initializing TwitterTrendsScraper.......")
        self.driver = WebDriver().get_driver()

    def login_with_cookie(self, auth_token) :
        cookie_dict = {
            'name': 'auth_token',
            'value': auth_token,
            'domain': '.twitter.com',
            'path': '/',
            'secure': True,
            'httpOnly': True
        }
        print("Logging in.......")
        self.driver.add_cookie(cookie_dict)

    def get_trends(self):
        print("preparing to get trends.......")
        trends_list = []
        self.driver.get(self.TWITTER_PATH_TRENDS)
        print("opening trends page.......")
        self.driver.refresh()
        self.driver.implicitly_wait(15)
        trend_data = self.driver.find_elements(By.CSS_SELECTOR, ".css-175oi2r.r-1adg3ll.r-1ny4l3l")[1:]
        print("Getting data started.......")
        for trend in trend_data:
            trend_info = {}
            try:
                trend_info['category'] = get_first_element_separator(trend.text, "\n")
            except NoSuchElementException:
                trend_info['category'] = None
            hashtags_element = trend.find_element(By.CSS_SELECTOR,
                                                  ".css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-b88u0q.r-1bymd8e")
            trend_info['text_trending'] = hashtags_element.text
            trend_info['type'] = "hashtag" if trend_info['text_trending'] and "#" in trend_info[
                'text_trending'] else "text"
            try:
                post_count_element = trend.find_element(By.CSS_SELECTOR,
                                                        ".css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-n6v787.r-1cwl3u0.r-16dba41.r-14gqq1x")
                trend_info['post_count'] = format_number(remove_char(post_count_element.text, " posts"))
            except NoSuchElementException:
                trend_info['post_count'] = None
            trend_info['scrapped_date'] = time.strftime("%Y-%m-%d %H:%M:%S")
            trends_list.append(trend_info)
        return trends_list

    def scrape_and_save_trends(self,cookie_value, output_file):
        try:
            self.driver.get(self.TWITTER_PATH)
            self.login_with_cookie(cookie_value)
            trends = self.get_trends()
            write_to_file(trends, output_file)
            self.driver.close()
            total_trends = len(trends)
            print(f"Success getting {total_trends} trends")
        except Exception as e:
            return f"Error: {e}"

    def __del__(self):
        print("Destroying TwitterTrendsScraper.......")
        WebDriver().close_driver()
