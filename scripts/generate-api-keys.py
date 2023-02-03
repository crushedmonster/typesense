import typesense
import uuid

# Initializing the client
client = typesense.Client({
  'nodes': [{
    'host': 'localhost', # For Typesense Cloud use xxx.a1.typesense.net
    'port': '8108',      # For Typesense Cloud use 443
    'protocol': 'http'   # For Typesense Cloud use https
  }],
  'api_key': 'xyz',
  'connection_timeout_seconds': 2
})

# Create API keys
# Reference: https://typesense.org/docs/0.24.0/api/api-keys.html#create-an-api-key
# Admin key
admin_key = client.keys.create({
  "description": "Admin key.",
  "actions": ["*"],
  "collections": ["*"]
})

# Search-only key
search_key = client.keys.create({
  "description": "Search-only companies key.",
  "actions": ["documents:search"],
  "collections": ["*"]
})

# Save keys
output = \
f"""=== Self-hosted Typesense ===

Admin API Key:
{admin_key["value"]}

Search Only API Key:
{search_key["value"]}
"""
run_id = uuid.uuid4().hex[:8]
filename = f"typesense-api-keys-{run_id}.txt"
with open(filename, 'w') as f:
    f.write(output)