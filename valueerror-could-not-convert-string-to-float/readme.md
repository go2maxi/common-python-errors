# ValueError: could not convert string to float

Occurs when converting a non-numeric string to a float.

## reproduce.py

```python
value = "abc"
number = float(value)
print(number)
```

## Error Message

```
ValueError: could not convert string to float: 'abc'
```

## Fix

```python
value = "abc"

if value.replace('.', '', 1).isdigit():
    number = float(value)
    print(number)
```

## Reflection

Got this while parsing input.
