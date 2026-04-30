Occurs when trying to parse empty content as JSON.

This can happen when:
- a file exists but is empty
- a string is empty ("")
- a string contains only whitespace (" ", "\n")

## reproduce

```python
import json

# data.json exists but is completely empty
with open('data.json', 'r') as f:
    data = json.load(f)
```

## Error message

```
JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

## Fix

```python
import json
import os

filename = 'data.json'

if os.path.exists(filename):
    with open(filename, 'r') as f:
        content = f.read()

        if content.strip():
            data = json.loads(content)
```

## Reflection

I initially thought the JSON file was corrupted.

It turned out the file existed but was empty, or sometimes only contained whitespace.

Checking the content before parsing helped avoid this specific "Expecting value" error.
