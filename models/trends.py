from configs.mongo import mongo_config

class TwitterTrends:
    def __init__(self):
        self.mongo = mongo_config()
        self.db = self.mongo.get_db()
        if not self.mongo.check_existence("trends"):
            self.mongo.create_collection("trends")
        self.collection = self.mongo.get_collection("trends")

    def save_trends(self, trends):
        try:
            self.collection.insert_many(trends)
            print("Trends saved successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def get_trends(self):
        try:
            trends = list(self.collection.find({}))
            print("Trends fetched successfully")
            return trends
        except Exception as e:
            print(f"Error: {e}")
            return False

    def delete_trends(self):
        try:
            self.collection.delete_many({})
            print("Trends deleted successfully")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

