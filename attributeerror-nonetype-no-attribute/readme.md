# AttributeError: 'NoneType' object has no attribute 'split'

Occurs when trying to call a method on a None value.

## reproduce.py

```python
name = None

print(name.split())
```

## Error Message

```
AttributeError: 'NoneType' object has no attribute 'split'
```

## Fix

```python
name = None

if name is not None:
    print(name.split())
```

## Reflection

Forgot to check for None before calling a method.

## Reference
- Related case: <https://pyai.io/en/python/basic/errors-and-tracebacks/>
