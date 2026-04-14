# JSONDecodeError: Expecting value

Occurs when trying to parse empty or invalid JSON data.

## Reproduce

```python
import json

data = ""

result = json.loads(data)
print(result)
```

## Error Message

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Fix

```python
import json

data = "{}"

result = json.loads(data)
print(result)
```

## Reflection

Tried to load it as JSON, but it turned out the data was just empty.
