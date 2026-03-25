import json
import os

filename = 'data.json'

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, 'r') as f:
        data = json.load(f)
