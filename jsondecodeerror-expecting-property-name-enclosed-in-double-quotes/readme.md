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
json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 1 column 18 (char 17)
```

## Fix

```python
import json

data = '{"name": "john", "age": 30}'

parsed = json.loads(data)
print(parsed)
```

## Reflection

Used invalid JSON format without quoting a property name. 
The error message specifically pointed to the location where the quote was missing.

