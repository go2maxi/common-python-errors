# FileExistsError: [Errno 17] File exists

## Reproduce

```python
import os

os.mkdir("test_dir")
os.mkdir("test_dir")
```

## Error Message

```
FileExistsError: [Errno 17] File exists: 'test_dir'
```

## Fix

```python
import os

if not os.path.exists("test_dir"):
    os.mkdir("test_dir")
```

## Reflection

I tried to create something that was already there.


## Reference

- Related case: <https://pyai.io/en/python/basic/file-io/>
