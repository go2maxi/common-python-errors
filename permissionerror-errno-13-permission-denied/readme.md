# PermissionError: [Errno 13] Permission denied

Occurs when trying to access a file without sufficient permissions.

'/root/test.txt' is a restricted path on Unix-based systems.

This occurs on Unix-based systems. On Windows, a different error may appear.

## reproduce.py

```python
# trying to write to a restricted location
with open('/root/test.txt', 'w') as f:
    f.write('hello')
```

## Error Message

```
PermissionError: [Errno 13] Permission denied: '/root/test.txt'
```

## Fix

```python
# writing to current directory instead
with open('test.txt', 'w') as f:
    f.write('hello')
```

## Reflection

Tried to write to a location without permission.
