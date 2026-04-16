# JSONDecodeError: Extra data

Occurs when multiple JSON objects are placed in a single string without proper structure.

## Reproduce

```python
import json

data = '{"name": "john"} {"age": 30}'

result = json.loads(data)
print(result)
```

## Error Message

```
json.decoder.JSONDecodeError: Extra data: line 1 column 18 (char 17)
```

## Fix

```python
import json

data = '[{"name": "john"}, {"age": 30}]'

result = json.loads(data)
print(result)
```

## Reflection

Tried to load multiple JSON objects at once, but JSON requires a single valid structure like an array or object.
