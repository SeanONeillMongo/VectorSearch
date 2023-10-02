# update_embeddings.py

import pymongo
import requests
from generate_embedding import generate_embedding  # Import the 'generate_embedding' function from generate_embedding.py

# Define the 'collection' variable here
client = pymongo.MongoClient("mongodb+srv://test:test@sandbox.8wtj44r.mongodb.net/")
db = client.sample_mflix
collection = db.movies

def update_embeddings():
    # You can now use 'generate_embedding' and 'collection' here
    for doc in collection.find({'plot': {"$exists": True}}).limit(50):
        doc['plot_embedding_hf'] = generate_embedding(doc['plot'])
        collection.replace_one({'_id': doc['_id']}, doc)

if __name__ == "__main__":
    update_embeddings()

# execute query
query = "imaginary characters from outer space at war"

results = collection.aggregate([
    {
        '$search': {
            "index": "PlotSemanticSearch",
            "knnBeta": {
                "vector": generate_embedding(query),
                "k": 4,
                "path": "plot_embedding_hf"}
        }
    }
])

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')
