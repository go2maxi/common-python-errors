# NotADirectoryError: [Errno 20] Not a directory: 'data.txt'

Occurs when using a file path where a directory is expected.

## Reproduce

```python
import os

file_path = "data.txt"

files = os.listdir(file_path)
print(files)
```

## Error Message

```
NotADirectoryError: [Errno 20] Not a directory: 'data.txt'
```

## Fix

```python
import os

folder_path = "."

files = os.listdir(folder_path)
print(files)
```

## Reflection

Tried listing contents of a file path as if it were a directory.
