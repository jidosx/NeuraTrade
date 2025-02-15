import pymongo

class MongoDBMemory:
    def __init__(self):
        self.client = None

    def connect_to_mongodb(self, uri):
        # Connect to MongoDB
        self.client = pymongo.MongoClient(uri)

    def store_data(self, data):
        # Store data in MongoDB
        db = self.client['neuratrade']
        collection = db['data']
        collection.insert_one(data)

    def retrieve_data(self):
        # Retrieve data from MongoDB
        db = self.client['neuratrade']
        collection = db['data']
        return collection.find()
