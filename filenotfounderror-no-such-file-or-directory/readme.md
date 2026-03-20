# FileNotFoundError: [Errno 2] No such file or directory

## Reproduce

```python
file_path = "data.txt"

f = open(file_path, "r")
```

## Error Message

FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'


## Fix

```python
file_path = "data.txt"

with open(file_path, "w") as f:
    f.write("sample")

with open(file_path, "r") as f:
    print(f.read())
```

## Reflection

I tried to read a file that didn’t exist yet.


## Reference

Related case: <https://pyai.io/en/python/basic/file-io/>

