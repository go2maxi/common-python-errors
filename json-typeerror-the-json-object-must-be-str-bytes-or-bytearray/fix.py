import json

data = {"name": "john", "age": 30}

# Convert dict to JSON string first
json_str = json.dumps(data)

result = json.loads(json_str)
print(result)
