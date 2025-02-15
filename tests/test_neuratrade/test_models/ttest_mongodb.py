import unittest
from neuratrade.memory.mongodb import MongoDBMemory
import pymongo

class TestMongoDBMemory(unittest.TestCase):
    def test_connect_to_mongodb(self):
        # Create MongoDB memory
        mongodb_memory = MongoDBMemory()

        # Connect to MongoDB
        mongodb_memory.connect_to_mongodb('mongodb://localhost:27017/')

        # Check if the connection is established
        self.assertIsNotNone(mongodb_memory.client)

    def test_store_data(self):
        # Create MongoDB memory
        mongodb_memory = MongoDBMemory()

        # Connect to MongoDB
        mongodb_memory.connect_to_mongodb('mongodb://localhost:27017/')

        # Create random data
        data = {'key': 'value'}

        # Store the data
        mongodb_memory.store_data(data)

        # Check if the data is stored
        db = mongodb_memory.client['neuratrade']
        collection = db['data']
        self.assertEqual(collection.count_documents({}), 1)

    def test_retrieve_data(self):
        # Create MongoDB memory
        mongodb_memory = MongoDBMemory()

        # Connect to MongoDB
        mongodb_memory.connect_to_mongodb('mongodb://localhost:27017/')

        # Create random data
        data = {'key': 'value'}

        # Store the data
        mongodb_memory.store_data(data)

        # Retrieve the data
        retrieved_data = mongodb_memory.retrieve_data()

        # Check if the data is retrieved
        self.assertEqual(retrieved_data.count(), 1)

if __name__ == '__main__':
    unittest.main()
