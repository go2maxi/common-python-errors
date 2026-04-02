# PermissionError: [Errno 13] Permission denied: '.'

Occurs when trying to perform a restricted operation on a directory.

## Reproduce

```python
import os

folder_path = "."

os.remove(folder_path)
```

## Error Message

```
PermissionError: [Errno 13] Permission denied: '.'
```

## Fix

```python
import os

file_path = "data.txt"

with open(file_path, "w") as file:
    file.write("hello")

os.remove(file_path)
```

## Reflection

Tried removing a directory as if it were a file.
