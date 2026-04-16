import json

# Fix: wrap multiple objects in a list
data = '[{"name": "john"}, {"age": 30}]'

result = json.loads(data)
print(result)
