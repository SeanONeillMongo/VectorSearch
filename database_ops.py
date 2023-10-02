import pymongo

client = pymongo.MongoClient("mongodb+srv://test:test@sandbox.8wtj44r.mongodb.net/")
db = client.sample_mflix
collection = db.movies

# Define functions for database operations
def insert_document(data):
    # Insert data into the MongoDB collection
    pass