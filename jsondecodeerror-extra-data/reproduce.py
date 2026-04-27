import json

# Invalid JSON: multiple JSON objects without proper structure
data = '{"name": "john"} {"age": 30}'

result = json.loads(data)
print(result)
