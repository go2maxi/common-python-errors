# IsADirectoryError: [Errno 21] Is a directory

Occurs when trying to open a directory as if it were a file.

## Reproduce

```python
import os

# Create a directory
os.makedirs("data_dir", exist_ok=True)

# Trying to open a directory as if it were a file
with open("data_dir", "r") as f:
    content = f.read()
```

## Error Message

```
IsADirectoryError: [Errno 21] Is a directory: 'data_dir'
```

## Fix

```python
import os

file_path = "data.txt"

# Ensure it's a file, not a directory
if os.path.isfile(file_path):
    with open(file_path, "r") as f:
        content = f.read()
        print(content)
else:
    print("Expected a file, but got a directory or missing file.")
```

## Reflection

Tried to open a folder like a file, but it wasn’t a regular file.
