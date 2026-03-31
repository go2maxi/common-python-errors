# KeyError: 'age'

Occurs when accessing a missing key in a dictionary.

## Reproduce

```python
data = {
    "name": "john"
}

age = data["age"]
print(age)
```

## Error Message

```
KeyError: 'age'
```

## Fix

```python
data = {
    "name": "john"
}

age = data.get("age", 0)
print(age)
```

## Reflection

Assumed the key existed without checking.
