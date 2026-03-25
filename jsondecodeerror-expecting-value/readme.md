# JSONDecodeError: Expecting value: line 1 column 1 (char 0)

Occurs when trying to parse an empty file or an empty string as JSON.

data.json exists but is completely empty.

## reproduce.py

```python
import json

# data.json exists but is completely empty
with open('data.json', 'r') as f:
    data = json.load(f)
```

## Error message

```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Fix

```python
import json
import os

filename = 'data.json'

if os.path.exists(filename) and os.path.getsize(filename) > 0:
    with open(filename, 'r') as f:
        data = json.load(f)
```

## Reflection

File was empty, so json.load failed.
