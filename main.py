from worker.trends import TwitterTrendsScraper
import os
import time
from dotenv import load_dotenv
load_dotenv(".env")


def main():
    text = r'''
     _____           _ _   _              _____                    _       __                                      
    /__   \__      _(_) |_| |_ ___ _ __  /__   \_ __ ___ _ __   __| |___  / _\ ___ _ __ __ _ _ __  _ __   ___ _ __ 
      / /\/\ \ /\ / / | __| __/ _ \ '__|   / /\/ '__/ _ \ '_ \ / _` / __| \ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
     / /    \ V  V /| | |_| ||  __/ |     / /  | | |  __/ | | | (_| \__ \ _\ \ (__| | | (_| | |_) | |_) |  __/ |   
     \/      \_/\_/ |_|\__|\__\___|_|     \/   |_|  \___|_| |_|\__,_|___/ \__/\___|_|  \__,_| .__/| .__/ \___|_|   
                                                                                            |_|   |_|              
    '''
    print(text)
    print("Version: 1.0.0")
    print("Description: This is a simple script to scrape Twitter trends and save to a file.")
    print("=========================================================================================")
    start_time = time.time()
    runner_trends()
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

def runner_trends():
    trends_worker = TwitterTrendsScraper()
    AUTH_TOKEN = os.getenv("TWITTER_AUTH_TOKEN")
    PATH_TO_SAVE = "temp/trends"+str(int(time.time()))+".json"
    trends_worker.scrape_and_save_trends(AUTH_TOKEN, PATH_TO_SAVE)
    print(f"Data written to {PATH_TO_SAVE} successfully.")

if __name__ == "__main__":
    main()


