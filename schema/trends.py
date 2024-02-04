from config import mongo

trends_schema = {
    "category": {
        "type": "string",
        "required": True
    },
    "hashtags": {
        "type": "list",
        "required": True
    },
    "trending_date": {
        "type": "string",
        "required": True
    },
    "post_count": {
        "type": "integer",
        "required": True
    },
    "scrapped_date": {
        "type": "string",
        "required": True
    }
}

collections_name = "trends"
validator = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["category", "hashtags", "trending_date", "post_count", "scrapped_date"],
        "properties": {
            "category": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "hashtags": {
                "bsonType": "array",
                "description": "must be an array and is required"
            },
            "trending_date": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "post_count": {
                "bsonType": "int",
                "description": "must be an integer and is required"
            },
            "scrapped_date": {
                "bsonType": "string",
                "description": "must be a string and is required"
            }
        }
    }
}

mongo_config = mongo.mongo_config()
db = mongo_config.get_db()
collection = mongo_config.get_collection(collections_name)

db.create_collection(collections_name, validator=validator)