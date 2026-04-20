# FileNotFoundError: wrong relative path

Occurs when the file exists, but Python can't find it from the current working directory.

## reproduce.py

```python
with open("data.txt", "r") as f:
    content = f.read()

print(content)
```

## Error message

```
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

## Fix

```python
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data.txt")

with open(file_path, "r") as f:
    content = f.read()

print(content)
```

## Reflection

Thought the file was in the same folder, but Python was running from a different location.

