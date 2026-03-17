# KeyError: 'age'

Occurs when accessing a dictionary key that does not exist.

## reproduce.py

```python
data = {"name": "John"}
print(data["age"])
```

## Error message

```
KeyError: 'age'
```

## fix.py

```python
data = {"name": "John"}
print(data.get("age"))
```

### Reflection
Use `.get()` to safely access dictionary keys that might not exist.