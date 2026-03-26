# AttributeError: 'dict' object has no attribute 'append'

Occurs when calling append() on a dictionary.

## Reproduce

```python
user_scores = {"math": 90}

print(user_scores)
user_scores.append(85)
```

## Error Message

```
AttributeError: 'dict' object has no attribute 'append'
```

## Fix

```python
user_scores = {"math": 90}

print(user_scores)
user_scores["english"] = 85
print(user_scores)
```

## Reflection

Tried using append() on a dict like a list.
