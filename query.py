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