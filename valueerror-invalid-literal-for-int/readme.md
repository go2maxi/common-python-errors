# ValueError: invalid literal for int()

Occurs when trying to convert a non-numeric string to an integer.

## reproduce.py

```python
value = "abc"
number = int(value)
print(number)
```

## Error message

```
ValueError: invalid literal for int() with base 10: 'abc'
```

## fix.py

```python
value = "123"
number = int(value)
print(number)
```

### Reflection
Ensure the string is a valid integer before converting to `int`.
