# TypeError: write() argument must be str, not dict

Occurs when writing non-string data to a file.

## Reproduce

```python
data = {
    "name": "john",
    "age": 30
}

with open("output.txt", "w") as file:
    file.write(data)
```

## Error Message

```
TypeError: write() argument must be str, not dict
```

## Fix

```python
import json

data = {
    "name": "john",
    "age": 30
}

with open("output.txt", "w") as file:
    file.write(json.dumps(data))
```

## Reflection

Tried to write a dict directly without converting it to a string.
