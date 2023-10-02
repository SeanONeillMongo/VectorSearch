# main.py
from database_ops import insert_document
from generate_embedding import generate_embedding

# Your main script logic here

# Example usage:
embedding = generate_embedding("MongoDB is awesome")
insert_document({"text": "MongoDB is awesome", "embedding": embedding})

# Other tasks or operations
