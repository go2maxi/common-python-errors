# AttributeError: 'NoneType' object has no attribute 'split'

I tried to call `.split()` on a variable that was `None`.

## reproduce.py

```python
username = None
parts = username.split("_")
print(parts)
```

## Error message

```
AttributeError: 'NoneType' object has no attribute 'split'
```

## fix.py

```python
username = None

if username is None:
    print("Username not available")
    username = ""

parts = username.split("_")
print(parts)
```

## Reflection
Forgot to check for None before calling a method.
