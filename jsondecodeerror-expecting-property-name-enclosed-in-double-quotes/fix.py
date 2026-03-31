import json

data = '{"name": "john", "age": 30}'

parsed = json.loads(data)
print(parsed)
