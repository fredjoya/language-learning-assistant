import chromadb

# Initialize the client
client = chromadb.Client()

# Create a collection
collection = client.create_collection("arabic_listening_comprehension")

# Add docs to the collection
# You can also update and delete docs. A row-based API is coming soon!
collection.add(
    documents=["document1", "document2"],  # We embed for you, or bring your own
    metadatas=[{"source": "notion"}, {"source": "google-docs"}],  # Filter on arbitrary metadata!
    ids=["doc1", "doc2"],  # Must be unique for each doc
)

# Query the collection
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"},  # Optional filter
    # where_document={"$contains": "search_string"}  # Optional filter
)

# Print the results
print(results)

