# FileNotFoundError: [Errno 2] No such file or directory

Occurs when trying to open a file that does not exist or has an incorrect path.

## Reproduce

```python
with open("data.txt", "r") as f:
    content = f.read()

print(content)
```

## Error Message

```
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
```

## Fix

```python
with open("data.txt", "w") as f:
    f.write("hello")

with open("data.txt", "r") as f:
    content = f.read()

print(content)
```

## Reflection

Tried to open the file, but it wasn’t in the folder I was running from.


## Reference

Related case: <https://pyai.io/en/python/basic/file-io/>
