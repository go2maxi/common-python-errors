# PermissionError: [Errno 13] Permission denied

Occurs when a file is being used by another process or access is restricted.

## Reproduce

```python
file_path = "data.csv"

# Make sure the file is open in another program (e.g. Excel)
with open(file_path, "w") as f:
    f.write("update data")
```

## Error Message

```
PermissionError: [Errno 13] Permission denied: 'data.csv'
```

## Fix

```python
file_path = "data.csv"

with open(file_path, "w") as f:
    f.write("fixed data")
```

## Reflection

Tried to update the file, but it was still open in another program.
