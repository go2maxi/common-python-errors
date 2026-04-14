import json

data = {"name": "john", "age": 30}

# Passing a dict directly instead of a JSON string
result = json.loads(data)
print(result)
