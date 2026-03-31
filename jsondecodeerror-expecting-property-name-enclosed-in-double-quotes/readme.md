# JSONDecodeError: Expecting property name enclosed in double quotes

Occurs when JSON format is invalid.

## Reproduce

```python
import json

data = '{"name": "john", age: 30}'

parsed = json.loads(data)
print(parsed)
```

## Error Message

```
JSONDecodeError: Expecting property name enclosed in double quotes
```

## Fix

```python
import json

data = '{"name": "john", "age": 30}'

parsed = json.loads(data)
print(parsed)
```

## Reflection

Used invalid JSON format without quoting property name.
