# NotADirectoryError: [Errno 20] Not a directory

Occurs when trying to use a file as if it were a directory.

## Reproduce

```python
import os

with open("data.txt", "w") as f:
    f.write("hello")

os.listdir("data.txt")
```

## Error Message

```
NotADirectoryError: [WinError 267] 디렉터리 이름이 올바르지 않습니다: 'data.txt'
```
Note: On Unix-based systems, this error may appear as: 
NotADirectoryError: [Errno 20] Not a directory: 'data.txt'


## Fix

```python
import os

os.makedirs("data_dir", exist_ok=True)

print(os.listdir("data_dir"))
```

## Reflection

Tried to treat a file like a folder, but it wasn’t a directory.
