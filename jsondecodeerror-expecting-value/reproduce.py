import json

# data.json exists but is completely empty
with open('data.json', 'r') as f:
    data = json.load(f)
