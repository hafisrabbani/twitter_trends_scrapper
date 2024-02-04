from pymongo import MongoClient
from dotenv import load_dotenv
import os

class mongo_config:
    def __init__(self):
        load_dotenv(".env")
        self.client = MongoClient(os.getenv('MONGOURI'))
        self.db = self.client[os.getenv('DBNAME')]

    def get_db(self):
        return self.db

    def get_collection(self, collection_name):
        return self.db[collection_name]
