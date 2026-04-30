import json
import os

filename = 'data.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()

        if content.strip():
            data = json.loads(content)
