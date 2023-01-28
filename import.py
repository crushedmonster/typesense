import typesense
import json

# Initializing the client
client = typesense.Client({
  'nodes': [{
    'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '8108',      # For Typesense Cloud use 443
    'protocol': 'http'   # For Typesense Cloud use https
  }],
  'api_key': '<API_KEY>', # Use the same API key that was used to start the Typesense server 
  'connection_timeout_seconds': 2
})

# Creating a "books" collection
books_schema = {
  'name': 'books',
  'fields': [
    {'name': 'title', 'type': 'string' },
    {'name': 'authors', 'type': 'string[]', 'facet': True },

    {'name': 'publication_year', 'type': 'int32', 'facet': True },
    {'name': 'ratings_count', 'type': 'int32' },
    {'name': 'average_rating', 'type': 'float' }
  ],
  'default_sorting_field': 'ratings_count'
}

client.collections.create(books_schema)

# Adding books to the collection
with open('data/books.jsonl', encoding="utf-8") as infile:
    for json_line in infile:
        book_document = json.loads(json_line)
        client.collections['books'].documents.create(book_document)
